import bcrypt


def is_valid_password(customer, password):
    return bcrypt.hashpw(str(password), str(customer.password)) == str(customer.password)
