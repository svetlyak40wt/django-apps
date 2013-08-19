django-apps
===========

Installation
------------

As usual. Place django_apps somewhere in your python path or install it using easy_install:

    easy_install django-apps

Then, add `django_apps` to the `INSTALLED_APPS`.

Usage
-----

In the any template use template tag `installed_apps` to receive a list
of installed apps along with some information about them.

I use following code in my template, to show apps names along with
their versions and descriptions.

    {% load apps_tags %}
    {% installed_apps as apps %}
    <table class="apps">
    {% for app in apps %}
        <tr>
            <td>{{ app.name }}</td>
            <td>{{ app.version }}</td>
            <td>{{ app.description }}</td>
        </tr>
    {% endfor %}
    </table>

Please, note, that descriptions are hardcoded into the code of the `django_apps`.

