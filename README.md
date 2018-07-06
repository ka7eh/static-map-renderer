
## A python script for creating static map images using Selenium and leaflet

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

| Name   	| Type   	| Description                                                                                                                                        	|
|--------	|--------	|----------------------------------------------------------------------------------------------------------------------------------------------------	|
| width  	| number 	| Image width                                                                                                                                        	|
| height 	| number 	| Image height                                                                                                                                       	|
| bounds 	| array  	|  An array of bottom-left and top-right corners of the map. Each corner is an array containg its latitude and longitude. 	|
| layers 	| array  	| An array of objects. Each object defines a layer to add to the map. See the table below for description of layer object.                           	|

#### Layer params:

| Name 	| Type   	| Description                                                            	|
|------	|--------	|------------------------------------------------------------------------	|
| type 	| string 	| Name of Leaflet layer method to use for creating the layer, e.g. `tileLayer`, `marker`, or `polygon` 	|
| args 	| array  	| List of args to pass to layer method specified in `type`               	|

Here is an example payload:

```json
{
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

This is an example call to the server using the sample payload mentioned above:

```bash
curl -X POST localhost:8000 -d '{"width": 1200, "height": 800, "bounds": [[51.52636784966738, -0.0384521484375], [51.48362785353601, -0.14144897460937]], "layers": [{"type": "tileLayer", "args": ["https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"]}, {"type": "marker", "args": [[51.5, -0.09]]}, {"type": "circle", "args": [[51.508, -0.11], 500, {"color": "red", "fillColor": "#f03", "fillOpacity": 0.5}]}, {"type": "polygon", "args": [[[51.509, -0.08], [51.503, -0.06], [51.51, -0.047]]]}]}' -o test.png
```

You can also use the docker image included with this repo for setting up your environment:

- Create a `.env` file and set the server port in it (see `.env-example`).
- Run `docker-compose up`
