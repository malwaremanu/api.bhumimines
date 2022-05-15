def check_login(request):
    print('-'*100)
    print('checking login status from login.py script ')
    print('-'*100)
    if not request.session:
        return redirect('accounts_login')
