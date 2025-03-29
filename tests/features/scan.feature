Feature: Scan API

  Scenario: Scan returns all files from path
    Given the API is running
    When I request a scan of the directory
    Then I should receive a list of files
    And the number of files should match the expected baseline

  Scenario: Each file contains required metadata
    Given the API is running
    When I request a scan of the directory
    Then each file in the response should include path, size, modified, and type

  Scenario: Scan returns metadata for random file
    Given the API is running
    When I request scan metadata for a random file
    Then I should receive metadata including path, size, and modified

  Scenario: Scan directory using curl
    Given the API is running
    When I curl the scan endpoint
    Then the curl response should include a list of files

  Scenario: Scan random file using curl
    Given the API is running
    When I curl the random file endpoint
    Then the curl response should include metadata for the file