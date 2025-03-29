Feature: Directory Scanning and File Metadata Lookup

  This feature verifies that the API can scan media folders and return metadata for all files
  or for a specific file path. It validates both full scan results and individual lookups
  using a known baseline dataset.

  Background:
    Given a baseline dataset of scanned files is available
    And the scan path is "/Users/jseanw/Desktop/Pictures"

  Scenario: Retrieve all scanned media files
    When I request a scan of the entire directory
    Then the API should return the same number of files as in the baseline

  Scenario: Retrieve metadata for a single file
    Given I select a known file from the baseline
    When I request metadata for that specific file
    Then the API should return the correct metadata for the file

  Scenario: Request metadata for a missing file
    When I request metadata for a file that does not exist
    Then the API should return a 404 error
