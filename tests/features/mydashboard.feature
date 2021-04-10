Feature: Sample Test on Mercury
    Scenario Outline: Validate Title
        Given I load the website
        When I go to "Our_Coaches.html" page
        Then Title "<page>" is visible
        And Close the browser
        Examples:
        |page |
        |Our Coaches|
