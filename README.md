
```json
config = {
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
        "https://api.tiles.mapbox.com/v4/mapbox.streets/{z}/{x}/{y}.png?access_token=pk.eyJ1IjoibWFwYm94IiwiYSI6ImNpejY4NXVycTA2emYycXBndHRqcmZ3N3gifQ.rJcFIG214AriISLbB6B5aw"
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

```bash
curl -X POST localhost:8000 -d '{"width": 1200, "height": 800, "bounds": [[51.52636784966738, -0.0384521484375], [51.48362785353601, -0.14144897460937]], "layers": [{"type": "tileLayer", "args": ["https://api.tiles.mapbox.com/v4/mapbox.streets/{z}/{x}/{y}.png?access_token=pk.eyJ1IjoibWFwYm94IiwiYSI6ImNpejY4NXVycTA2emYycXBndHRqcmZ3N3gifQ.rJcFIG214AriISLbB6B5aw"]}, {"type": "marker", "args": [[51.5, -0.09]]}, {"type": "circle", "args": [[51.508, -0.11], 500, {"color": "red", "fillColor": "#f03", "fillOpacity": 0.5}]}, {"type": "polygon", "args": [[[51.509, -0.08], [51.503, -0.06], [51.51, -0.047]]]}]}' -o test.png
```