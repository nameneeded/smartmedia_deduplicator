import os
from behave import given, when, then

@given('the project structure script is present')
def step_impl(context):
    assert os.path.exists("scripts/generate_project_structure_tree.py")

@when('I run the script')
def step_impl(context):
    os.system("python scripts/generate_project_structure_tree.py")

@then('a file called "project_structure.md" should exist in the "docs" folder')
def step_impl(context):
    assert os.path.exists("docs/project_structure.md")