<h1 align='center'>Software Engineering Milestone 2</h1>

<p>For the second Milestone we have use full Django's power. In order to use full CRUD operations on Doctors and Patients
 we have used Django Admin page.</p>
<br>
<p>For this project we have made foundation for future Backend-Fronted JWT authorization, but yet did not connect it.
</p>

<h2 align='center'>In order to run project:</h2>
<ol type="1">
   <li>Download source code from GitHub.</li>
   <li>Run "pip install -r requirements.txt".</li>
   <li>Open Terminal and go to project folder.</li>
   <li>Run command: "python manage.py makemigrations"</li>
   <li>Run command: "python manage.py migrate"</li>
    <li>Run command: "python manage.py createsuperuser" - this is essential to create Admin user</li>
   <li>Run command: "python manage.py runserver"</li>
</ol>

<p>Now you can go to <i>localhost:8000/admin/</i> and login under your credentials.</p>

<p>Here you can create patients, doctors and perform all CRUD operations.</p>