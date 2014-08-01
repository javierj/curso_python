
Feature: updating quality of the products
   I, as inkeeper
   want to update the quality of the products
   to obtain the right price


    Scenario: updating quality's product
      Given Product "Red wine" with quality "45" and sell days "5"
      When Updating the quality of products
      Then Expected a quality of "44"
      And Expected sells days "4"

    Scenario: quality never decreases from 0
      Given Product "Red wine" with quality "0" and sell days "5"
      When Updating the quality of products
      Then Expected a quality of "0"
      And Expected sells days "4"
