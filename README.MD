A very basic website, written using django.

- database implemented using admin features of django
- show appropriate data, depending on the url. I tried to make it as flexible as possible, avoiding where possible hardcoding codes. Only on the summary page did I hardcode the names.
- In the sitesScreen/views are 3 different implementation of Sum and Avg. By default I have used the full SQL version, because I assume they are faster. The code in SitesScreen/urls can be changed from views.average to views.python_average for the python implementation.
