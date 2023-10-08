from django import template

register = template.Library()

@register.filter
def multiply(value, arg):
    try:
        result = float(value) * float(arg)
        if result.is_integer():
            return str(int(result))

        # Find the first non-zero digit after the decimal point.
        decimal_part = str(result).split('.')[1]
        significant_decimal = len(decimal_part) - len(decimal_part.rstrip('0'))

        # Return the result rounded to the position of the first non-zero digit.
        return f"{result:.{significant_decimal}f}"
    except (ValueError, TypeError):
        return 0
