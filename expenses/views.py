from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib import messages
from django.db.models import Sum
from .models import Expense
from .forms import ExpenseForm, RegisterForm

def register_view(request):
    if request.user.is_authenticated:
        return redirect('index')
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f"Welcome, {user.username}! Your account is ready.")
            return redirect('index')
    else:
        form = RegisterForm()
    return render(request, 'expenses/register.html', {'form': form})


@login_required
def index(request):
    # CREATE: Handle new expense form
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.user = request.user
            expense.save()
            messages.success(request, f"Added '{expense.title}' (₹{expense.amount}).")
            return redirect('index')
    else:
        form = ExpenseForm()

    # READ: Base queryset restricted to the logged-in user
    expenses = Expense.objects.filter(user=request.user).order_by('-date', '-id')

    # FILTER: Search & Category GET parameters
    search_query = request.GET.get('q', '').strip()
    selected_category = request.GET.get('category', '')

    if search_query:
        expenses = expenses.filter(title__icontains=search_query)
    if selected_category:
        expenses = expenses.filter(category=selected_category)

    # AGGREGATE: Total & Category breakdown for Chart.js
    total_spent = expenses.aggregate(Sum('amount'))['amount__sum'] or 0
    category_data = (
        expenses.values('category')
        .annotate(total=Sum('amount'))
        .order_by('-total')
    )

    chart_labels = [item['category'] for item in category_data]
    chart_totals = [float(item['total']) for item in category_data]

    context = {
        'form': form,
        'expenses': expenses,
        'total_spent': total_spent,
        'categories': Expense.CATEGORY_CHOICES,
        'selected_category': selected_category,
        'search_query': search_query,
        'chart_labels': chart_labels,
        'chart_totals': chart_totals,
    }
    return render(request, 'expenses/index.html', context)


@login_required
def edit_expense(request, expense_id):
    # Ensure user can ONLY edit their own expense
    expense = get_object_or_404(Expense, id=expense_id, user=request.user)
    
    if request.method == 'POST':
        form = ExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            messages.success(request, f"Updated '{expense.title}'.")
            return redirect('index')
    else:
        form = ExpenseForm(instance=expense)

    return render(request, 'expenses/edit.html', {'form': form, 'expense': expense})


@login_required
def delete_expense(request, expense_id):
    expense = get_object_or_404(Expense, id=expense_id, user=request.user)
    if request.method == 'POST':
        title = expense.title
        expense.delete()
        messages.warning(request, f"Deleted '{title}'.")
    return redirect('index')