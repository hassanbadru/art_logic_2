
# Decode Vector Instruction String - Art+Logic Exercise

## Description
Using the decoding function written for Part 1 submission to decode and describe a set of simple commands to build a vector-based drawing system.


## Set Up / Running App
- Download & unpack Hassan_Badru_Part2.zip file
- (*Recommended*) Install & run a Virtual Environment (e.g. `source Art_Logic_Env/bin/activate `)
- Assuming you already have *python* and *pip*, install requirements using `​ pip install -r requirements.txt` within command prompt or terminal *(if not, check out [How to install python & pip ](https://pip.pypa.io/en/stable/installing/))*
- Assuming you already have *Node* or *NPM*, inside the **frontend** folder, install node_modules (dependencies) using `npm install`  *(if not, check out [How to install Node ](https://nodejs.org/en/download/package-manager/))*
- To start server, run the command `python manage.py runserver`
- On your browser, go to http://127.0.0.1:8000/ or local server address provided within terminal

*Note: On your browser, go to http://127.0.0.1:8000/api to access REST API*

## Task
If the pen is moved while it is down, we draw along the line of motion in the current color. If the pen is moved while it is up, no drawing is done

The commands supported in this mini-language are:
- [x] Clear the drawing and reset all parameters
- [x] Raise/lower the pen
- [x] Change the current color
- [x] Move the pen

Commands are represented in the data stream by a single (un-encoded) opcode byte that can be identified by always having its most significant bit set, followed by zero or more bytes containing encoded data values. 

Any unrecognized commands encountered in an input stream should be ignored.

## Commands
Here are command formats used

| Command       | CLR          |
| ------------- |------------- |
| Opcode        | FO           |
| Parameters    | (None)       |
| Output        | CLR;\n       |

| Command       | PEN          |
| ------------- |------------- |
| Opcode        | 9O           |
| Parameters    | 0=up,not 0=down |
| Output        | PEN UP or PEN DOWN |

| Command       | CO |
| ------------- |------------- |
| Opcode        | AO           |
| Parameters    |  R G B A        |
| Output        | CO {r} {g} {b} {a}      |

| Command       | MV           |
| ------------- |------------- |
| Opcode        | CO           |
| Parameters    | dx0 dy0 [dx1 dy1 .. dxn dyn] |
| Output        | MV (xo, y0) (x1, y1) [... (xn, yn)]    |

## Technology Stack Used
* ##### HTML5 / CSS (View Template)
* ##### REACT JS (Frontend)
* ##### Django / Python (Backend)
* ##### PostgreSQL (Database)
* ##### Django REST Framework (API)
* ##### Node / NPM (Production Build)

## Structure
- ### Model
```
class UserAction(models.Model):
    operation = models.CharField(max_length=100, default='encoding')
    input = models.CharField(max_length=100, default='8191')
    result = models.CharField(max_length=100, default='')
```
- ### View
```
class ArtLogicAPI(generics.ListCreateAPIView):
    queryset = UserAction.objects.all()
    serializer_class = UserActionSerializer


class ArtLogicApp(TemplateView):
    template_name = 'index.html'
```
- ### Template
I set the template use to load from React's production build folder in *settings.py*
`'DIRS': [ os.path.join(BASE_DIR, 'frontend/build') ],`

- ### Utility (MyFunction.py)
#### Encoding Function:
```
def encoder(input_num):
    ....
    return output
```
#### Decoding function:
```
def decoder(input_num):
    ....
    return output
```

#### Get function:
```
def get_instructions(m_string):
    ....
    return output
```

#### Read function:
```
def readInstruction(s1):
    ....
    return output
```

#### Boundary Fix function:
```
def def fix_boundary(val):
    ....
    return output
```

#### Write function:
```
def write_instructions(instruction_stream):
    ....
    return output
```




- ### Routing
Django Project:
```
urlpatterns = [
  url(r'^admin/', admin.site.urls),
  url(r'^', include('art_logic_app.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```
Django App (art_logic_app):
```
    url('api/', views.ArtLogicAPI.as_view() ),
    url(r'^$', views.ArtLogicApp.as_view(), name="art_logic" )
```

- ### API / Serialization
```
class UserActionSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAction
        fields = ('operation', 'input', 'result')
```



## How the App Works
### REACT Single Page

#### Input Instruction Screen
![alt text](https://docs.google.com/uc?id=1RM-ZU_RQ4dWYCEm7WO6Arz656FEgvV7k "screenshot1")

#### Decoded Instruction Screen & Graph
![alt text](https://docs.google.com/uc?id=12o58b4MLzxModf9YKqGqbQQUziklyNFS "screenshot2")

## Features
* User can select what kind of operation they want to perform
* After selecting operation, user can input values they want to encode/decode
* The app checks if user inputted a correctly formatted (valid) values i.e.
    > 14-bit signed integer (when encoding)

    > 16-bit hexadecimal decimal value for decoding
* Error Handling: Users get error messages if invalid values were inputted
* If no errors, the result of the encoding or decoding operation is outputted & displays.
* The app reads stored data (for encoding/decoding) in database and then uses the data object attributes to compute results
* Allows user to download convertedData.txt file containing encoding/decoding data of preloaded values
* The app keeps a record of every valid operation performed by the user and serializes it for the API

## Folder Structure
```
Hassan_Badru_Part2
    ├── README.md
    ├── art_logic
    │   ├── __init__.py
    │   ├── settings.py
    │   ├── urls.py
    │   ├── wsgi.py
    ├── art_logic_app
    │   ├── __init__.py
    │   ├── admin.py
    │   ├── apps.py
    │   ├── fixtures
    │   │   └── art_logic_app.json
    │   ├── migrations
    │   │   ├── 0001_initial.py
    │   │   ├── 0002_auto_20180515_2039.py
    │   │   ├── 0003_auto_20180519_2226.py
    │   │   ├── __init__.py
    │   │   └── __init__.pyc
    │   ├── models.py
    │   ├── myfunctions.py
    │   ├── serializers.py
    │   ├── tests.py
    │   ├── urls.py
    │   ├── views.py
    ├── db.sqlite3
    ├── frontend
    │   ├── README.md
    │   ├── build
    │   │   ├── asset-manifest.json
    │   │   ├── favicon.ico
    │   │   ├── index.html
    │   │   ├── manifest.json
    │   │   ├── service-worker.js
    │   │   └── static
    │   │       ├── css
    │   │       │   ├── main.a203576f.css
    │   │       │   └── main.a203576f.css.map
    │   │       ├── js
    │   │       │   ├── main.c96fb44e.js
    │   │       │   └── main.c96fb44e.js.map
    │   │       └── media
    │   │           └── intro-bg.fb30f247.jpg
    │   ├──
    │   ├── package.json
    │   ├── public
    │   │   ├── favicon.ico
    │   │   ├── index.html
    │   │   └── manifest.json
    │   ├── src
    │   │   ├── App.js
    │   │   ├── App.test.js
    │   │   ├── css
    │   │   │   ├── App.css
    │   │   │   └── index.css
    │   │   ├── img
    │   │   │   └── intro-bg.jpg
    │   │   ├── index.js
    │   │   ├── logo.svg
    │   │   └── registerServiceWorker.js
    │   └── yarn.lock
    ├── requirements.txt
    ├── manage.py
    └── media
        └── ConvertedData.txt
```

## Extensibility
- An added feature in the future could allow the userto toggle between user text input or file input
![alt text](https://docs.google.com/uc?id=1KpToCfgzJh__eUMxtZGlPydJgs9XojC8 "screenshot_2")
