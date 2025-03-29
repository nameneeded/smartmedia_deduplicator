Feature: Project structure generation
  As a developer
  I want to generate a markdown file of my project tree
  So that I can track structural changes over time

  Scenario: Running the project structure script
    Given the project structure script is present
    When I run the script
    Then a file called "project_structure.md" should exist in the "docs" folder