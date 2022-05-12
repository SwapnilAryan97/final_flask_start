{% extends "base.html" %}
{% from 'bootstrap5/table.html' import render_table %}
{% from "bootstrap5/pagination.html" import render_pagination %}


<div class="row col-8">
    {% block title %}Browse: {{ record_type }}{% endblock %}
    {% block content %}

                <a href="{{ url_for("transactions.transactions_upload") }}" class="btn col-3 mb-5 btn-info" role="button">Upload Transactions</a>

        <h2>Browse: Transactions</h2>
        <h2>The available balance is : {{ user_balance }}</h2>
        {{ render_table(data, titles=[('id','id'), ('Transaction Amount','Transaction Amount'), ('Transaction Type', 'Transaction Type'), ('Transaction User', 'Transaction User')]) }}
        {% from 'bootstrap5/pagination.html' import render_pagination %}

        {{ render_pagination(pagination) }}
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
    <script src="https://cdn.datatables.net/1.11.5/js/jquery.dataTables.min.js"></script>
    <script src="https://cdn.datatables.net/1.11.5/js/dataTables.bootstrap5.min.js"></script>
        <script type=text/javascript>
            $(document).ready(function () {
                $('.table').DataTable();
            });
        </script>



    {% endblock %}
</div>
