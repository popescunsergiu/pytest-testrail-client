**********************
pytest-testrail-client
**********************

pytest-testrail-client is a plugin for pytest_ that provides integration of pytest and pytest-bdd with TestRail

It provides capabilities of exporting Test Cases and Test Results to TestRail

.. contents:: **Table of Contents**
    :depth: 4

Requirements
============

Following prerequisites are needed in order to use pytest-testrail-client:

- cucumber-tag-expressions >= 2.0.0
- gherkin-official >= 4.1.0
- pytest >= 4.2
- pytest-bdd >= 3.3.0
- requests

Installation
============

To install pytest-testrail-client:

.. code-block::

  pip install pytest-testrail-client

Features and Usage
==================

TestRail Configuration
----------------------

pytest-testrail-client configuration data can be provided in three different ways:

- By using Environment Variables:
    .. code-block::

        TESTRAIL_URL=[URL of TestRail instance]
        TESTRAIL_EMAIL= [email [of user to be used for communication]]
        TESTRAIL_KEY=key [of user to be used for communication]
        TESTRAIL_PROJECT_ID=[project id to which the data is sent]
        JIRA_PROJECT_KEY=[Jira project key for integration with Jira]

- By using command line arguments:
    .. code-block::

        --pytest-testrail-client True / False
        --testrail-url [URL of TestRail instance]
        --testrail-email [email [of user to be used for communication]]
        --testrail-key key [of user to be used for communication]
        --testrail-project-id [project id to which the data is sent]
        --jira-project-key [Jira project key for integration with Jira]

- By using *pytest.ini* file:
    .. code-block::

        [pytest-testrail-client]
        pytest-testrail-client = True / False
        testrail-url = [URL of TestRail instance]
        testrail-email = [email [of user to be used for communication]]
        testrail-key = key [of user to be used for communication]
        testrail-project-id = [project id to which the data is sent]
        jira-project-key = [Jira project key for integration with Jira]

Note:
- Please follow TestRail instructions for generating user_key_
- Jira integration is done with `TestRail for Jira Test Management`_
- TestRail Project type shall be `Multiple Test Suites to manage cases`_

Export Test Cases to TestRail
-----------------------------

.. code-block::

    python -m pytest -v --pytest-testrail-export-test-cases --pytest-testrail-feature-files-relative-path "features"

Read more about *TestRail* `Test Suites and Cases`_

Implementation details
++++++++++++++++++++++

TODO

Export Tests to TestRail
------------------------

.. code-block::

    python -m pytest ./tests -v --pytest-testrail-export-test-results --pytest-testrail-test-plan-id [ID of Plan to be used] --pytest-testrail-test-configuration-name [str: Id of Test Configuration to be used]

Read more about *TestRail* `Test Plans and Configurations`_


Implementation details
++++++++++++++++++++++

TODO

Resources
=========

.. _pytest: http://pytest.org
.. _user_key: http://docs.gurock.com/testrail-api2/accessing
.. _TestRail for Jira Test Management: https://marketplace.atlassian.com/apps/1213701/testrail-for-jira-test-management?hosting=cloud&tab=overview
.. _Multiple Test Suites to manage cases: https://www.gurock.com/testrail/videos/project-types

.. _Test Suites and Cases: https://www.gurock.com/testrail/videos/suites-test-cases
.. _Test Plans and Configurations: https://www.gurock.com/testrail/videos/test-plans-configurations
