from django import template

register = template.Library()

@register.simple_tag
def case_count_in_suite(suite):
    return suite.cases.count()

@register.simple_tag
def case_run_successandfailure(runs):
    passed = 0
    failed = 0
    if runs:
        for item in runs.all():
            if item.ret_code != 0:
                failed += 1
            else:
                passed += 1
    return passed, failed


