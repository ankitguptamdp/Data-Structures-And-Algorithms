
<a name="readme-top"></a>

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/ankitguptamdp/Data-Structures-and-Algorithms/">
    <img src="Resources/Images/Data-Structures-and-Algorithms.jpg" alt="Logo" width="200" height="100">
  </a>

  <h3 align="center">Data-Structures-and-Algorithms</h3>

  <p align="center">
    A repository that contains all the Data Structures and Algorithms concepts 
    <br />
    And solutions to various problems in Python3 stored in a structured manner !
    <br />
    <a href="https://github.com/ankitguptamdp/Data-Structures-and-Algorithms/tree/main/Documents/"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/ankitguptamdp/Data-Structures-and-Algorithms/tree/main/Codes/">View Codes</a>
    ·
    <a href="mailto:ankitguptamdp@gmail.com">Report Bug</a>
    ·
    <a href="mailto:ankitguptamdp@gmail.com">Request Feature</a>
  </p>
</div>

| # | Problem | Solution | Difficulty | Status | Tags |
| --- | --- | --- | --- | --- | --- |
| 0019 | [Remove Nth Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list/) |  [Solution](https://github.com/ankitguptamdp/Data-Structures-and-Algorithms/blob/main/Codes/Binary%20Search%20Tree/Validate%20Binary%20Search%20Tree.py) | Medium | Solved | Linked List, Two Pointers |


<!DOCTYPE html>
<html>
<head>
  <title>Sorted Table</title>
  <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
  <script>
    $(document).ready(function() {
      function sortTable(column) {
        var $table = $('#table');
        var $rows = $table.find('tbody > tr');

        $rows.sort(function(a, b) {
          var aValue = $(a).find('td').eq(column).text();
          var bValue = $(b).find('td').eq(column).text();
          return aValue.localeCompare(bValue);
        });

        $table.find('tbody').empty().append($rows);
      }

      $('th').click(function() {
        var index = $(this).index();
        sortTable(index);
      });
    });
  </script>
  <style>
    table {
      border-collapse: collapse;
    }

    th,
    td {
      border: 1px solid black;
      padding: 8px;
      cursor: pointer;
    }
  </style>
</head>
<body>
  <table id="table">
    <!-- Replace this section with your generated table -->
    <thead>
      <tr>
        <th>Name</th>
        <th>Age</th>
        <th>Country</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>John</td>
        <td>25</td>
        <td>USA</td>
      </tr>
      <tr>
        <td>Alice</td>
        <td>32</td>
        <td>Canada</td>
      </tr>
      <tr>
        <td>David</td>
        <td>28</td>
        <td>Australia</td>
      </tr>
    </tbody>
    <!-- End of generated table -->
  </table>
</body>
</html>

