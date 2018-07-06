
## A python script for creating static map images using Selenium and leaflet/mapbox-gl-js

### Dependencies:

- A display server supported by [PyVirtualDisplay](https://pypi.org/project/PyVirtualDisplay/): [XVFB](https://www.x.org/releases/X11R7.7/doc/man/man1/Xvfb.1.xhtml), [Xephyr](https://freedesktop.org/wiki/Software/Xephyr/), or [Xvnc](https://www.hep.phy.cam.ac.uk/vnc_docs/xvnc.html) (the script is only tested with XVFB)
- [Firefox](https://www.mozilla.org/en-US/firefox/new/)
- [Gecko driver](https://github.com/mozilla/geckodriver/releases)

### Usage

Create a python 3 virtual environment and then install packages in `requirements.txt`:

> `pip install -r src/requirements.txt`

Then start the server by running `python server.py` in `src` folder.

After the server started, you can send post requests to `localhost:8000` with a payload with the following parameters:

#### Payload params:

| Name   	    | Type   | Description                                                                                                                    |
|-------------|--------|--------------------------------------------------------------------------------------------------------------------------------|
| renderer    | string | Renderer to use: `leaflet` or `mapbox` (default is `leaflet`)                                                                  |
| width  	    | number | Image width                                                                                                                    |
| height 	    | number | Image height                                                                                                                   |
| mapboxToken | string | Access token for mapbox-gl                                                                                                     |
| style       | string | Style url for mapbox-gl                                                                                                        |
| bounds 	    | array  | An array of bottom-left and top-right corners of the map. Each corner is an array containg its latitude and longitude          |
| layers 	    | array  | An array of objects. Each object defines a layer to add to the map. See the following sections for description of layer object |

#### Leaflet layer params:

| Name 	| Type   	| Description                                                            	                             |
|------	|--------	|------------------------------------------------------------------------------------------------------|
| type 	| string 	| Name of Leaflet layer method to use for creating the layer, e.g. `tileLayer`, `marker`, or `polygon` |
| args 	| array  	| List of args to pass to layer method specified in `type`               	                             |

Here is an example payload for leaflet:

```json
{
  "renderer": "leaflet",
  "width": 1200,
  "height": 800,
  "bounds": [
      [
        51.52636784966738,
        -0.03845214843750,
      ],
      [
        51.48362785353601,
        -0.14144897460937
      ]
  ],
  "layers": [
    {
      "type": "tileLayer",
      "args": [
        "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
      ]
    },
    {
      "type": "marker",
      "args": [
        [
          51.5,
          -0.09
        ]
      ]
    },
    {
      "type": "circle",
      "args": [
        [
          51.508,
          -0.11
        ],
        500,
        {
          "color": "red",
          "fillColor": "#f03",
          "fillOpacity": 0.5
        }
      ]
    },
    {
      "type": "polygon",
      "args": [
        [
          [
            51.509,
            -0.08
          ],
          [
            51.503,
            -0.06
          ],
          [
            51.51,
            -0.047
          ]
        ]
      ]
    }
  ]
}
```

Test it with curl:

```bash
curl -X POST localhost:8000 -d '{"width": 1200, "height": 800, "bounds": [[51.52636784966738, -0.0384521484375], [51.48362785353601, -0.14144897460937]], "layers": [{"type": "tileLayer", "args": ["https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"]}, {"type": "marker", "args": [[51.5, -0.09]]}, {"type": "circle", "args": [[51.508, -0.11], 500, {"color": "red", "fillColor": "#f03", "fillOpacity": 0.5}]}, {"type": "polygon", "args": [[[51.509, -0.08], [51.503, -0.06], [51.51, -0.047]]]}]}' -o test.png
```

#### Mapbox-GL layer :

Each object in `layers` array must be a valid Mapbox GL JS layer. See Mapbox documentation for more details: [https://www.mapbox.com/mapbox-gl-js/api/](https://www.mapbox.com/mapbox-gl-js/api/)

This is an example payload for mapbox-gl:

```json
{
  "renderer": "mapbox",
  "width": 1200,
  "height": 800,
  "mapboxToken": "your-mapbox-access-token",
  "style": "mapbox://styles/mapbox/streets-v9",
  "bounds": [
      [
        -90.1649314032637,
        41.88792273952086
      ],
      [
        -46.10975562201165,
        48.21182390952387
      ]
  ],
  "layers": [
    {
      "id": "maine",
      "type": "fill",
      "source": {
        "type": "geojson",
        "data": {
          "type": "Feature",
          "geometry": {
            "type": "Polygon",
            "coordinates": [
              [
                [
                  -67.13734351262877,
                  45.137451890638886
                ],
                [
                  -66.96466,
                  44.8097
                ],
                [
                  -68.03252,
                  44.3252
                ],
                [
                  -69.06,
                  43.98
                ],
                [
                  -70.11617,
                  43.68405
                ],
                [
                  -70.64573401557249,
                  43.090083319667144
                ],
                [
                  -70.75102474636725,
                  43.08003225358635
                ],
                [
                  -70.79761105007827,
                  43.21973948828747
                ],
                [
                  -70.98176001655037,
                  43.36789581966826
                ],
                [
                  -70.94416541205806,
                  43.46633942318431
                ],
                [
                  -71.08482,
                  45.3052400000002
                ],
                [
                  -70.6600225491012,
                  45.46022288673396
                ],
                [
                  -70.30495378282376,
                  45.914794623389355
                ],
                [
                  -70.00014034695016,
                  46.69317088478567
                ],
                [
                  -69.23708614772835,
                  47.44777598732787
                ],
                [
                  -68.90478084987546,
                  47.184794623394396
                ],
                [
                  -68.23430497910454,
                  47.35462921812177
                ],
                [
                  -67.79035274928509,
                  47.066248887716995
                ],
                [
                  -67.79141211614706,
                  45.702585354182816
                ],
                [
                  -67.13734351262877,
                  45.137451890638886
                ]
              ]
            ]
          }
        }
      },
      "layout": {},
      "paint": {
        "fill-color": "#088",
        "fill-opacity": 0.8
      }
    },
    {
      "id": "rect",
      "type": "fill",
      "source": {
        "type": "geojson",
        "data": {
          "type": "Feature",
          "geometry": {
            "type": "Polygon",
            "coordinates": [
              [
                [
                  -66.55517578125,
                  43.44494295526125
                ],
                [
                  -64.27001953125,
                  43.44494295526125
                ],
                [
                  -64.27001953125,
                  44.59829048984011
                ],
                [
                  -66.55517578125,
                  44.59829048984011
                ],
                [
                  -66.55517578125,
                  43.44494295526125
                ]
              ]
            ]
          }
        }
      },
      "layout": {},
      "paint": {
        "fill-color": "#088",
        "fill-opacity": 0.8
      }
    }
  ]
}
```

Test it with curl (replace `<mapbox-token>` with your own Mapbox access token):

```bash
curl -X POST localhost:8000 -d '{"renderer": "mapbox", "width": 1200, "height": 800, "mapboxToken": "<mapbox-token>", "style": "mapbox://styles/mapbox/streets-v9", "bounds": [[-90.1649314032637, 41.88792273952086], [-46.10975562201165, 48.21182390952387]], "layers": [{"id": "maine", "type": "fill", "source": {"type": "geojson", "data": {"type": "Feature", "geometry": {"type": "Polygon", "coordinates": [[[-67.13734351262877, 45.137451890638886], [-66.96466, 44.8097], [-68.03252, 44.3252], [-69.06, 43.98], [-70.11617, 43.68405], [-70.64573401557249, 43.090083319667144], [-70.75102474636725, 43.08003225358635], [-70.79761105007827, 43.21973948828747], [-70.98176001655037, 43.36789581966826], [-70.94416541205806, 43.46633942318431], [-71.08482, 45.3052400000002], [-70.6600225491012, 45.46022288673396], [-70.30495378282376, 45.914794623389355], [-70.00014034695016, 46.69317088478567], [-69.23708614772835, 47.44777598732787], [-68.90478084987546, 47.184794623394396], [-68.23430497910454, 47.35462921812177], [-67.79035274928509, 47.066248887716995], [-67.79141211614706, 45.702585354182816], [-67.13734351262877, 45.137451890638886]]]}}}, "layout": {}, "paint": {"fill-color": "#088", "fill-opacity": 0.8}},{"id": "rect", "type": "fill", "source": {"type": "geojson", "data": {"type": "Feature", "geometry": {"type": "Polygon", "coordinates": [[[-66.55517578125, 43.44494295526125], [-64.27001953125, 43.44494295526125], [-64.27001953125, 44.59829048984011], [-66.55517578125, 44.59829048984011], [-66.55517578125, 43.44494295526125]]]}}}, "layout": {}, "paint": {"fill-color": "#088", "fill-opacity": 0.8}}]}' -o test.png
```

You can also use the docker image included with this repo for setting up your environment:

- Create a `.env` file and set the server port in it (see `.env-example`)
- Run `docker-compose up`
