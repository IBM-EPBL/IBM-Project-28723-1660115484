[
    {
        "id": "931153a67f419cc7",
        "type": "tab",
        "label": "Flow 1",
        "disabled": false,
        "info": "",
        "env": []
    },
    {
        "id": "1f76e7a65e8d65a7",
        "type": "ibmiot in",
        "z": "931153a67f419cc7",
        "authentication": "apiKey",
        "apiKey": "b2ede069630b4886",
        "inputType": "evt",
        "logicalInterface": "",
        "ruleId": "",
        "deviceId": "DeviceID1",
        "applicationId": "",
        "deviceType": "Devicetype1",
        "eventType": "+",
        "commandType": "",
        "format": "json",
        "name": "IBM IoT",
        "service": "registered",
        "allDevices": "",
        "allApplications": "",
        "allDeviceTypes": "",
        "allLogicalInterfaces": "",
        "allEvents": true,
        "allCommands": "",
        "allFormats": "",
        "qos": 0,
        "x": 70,
        "y": 20,
        "wires": [
            [
                "dd48d91014d7df34",
                "2c5830d11ddd6bf5",
                "12731096ae105ada"
            ]
        ]
    },
    {
        "id": "dd48d91014d7df34",
        "type": "debug",
        "z": "931153a67f419cc7",
        "name": "",
        "active": false,
        "tosidebar": true,
        "console": false,
        "tostatus": false,
        "complete": "payload",
        "targetType": "msg",
        "statusVal": "",
        "statusType": "auto",
        "x": 430,
        "y": 20,
        "wires": []
    },
    {
        "id": "2c5830d11ddd6bf5",
        "type": "function",
        "z": "931153a67f419cc7",
        "name": "Temperature node",
        "func": "msg.payload = msg.payload.Temperature\nglobal.set('t', msg.payload)\nreturn msg;",
        "outputs": 1,
        "noerr": 0,
        "initialize": "",
        "finalize": "",
        "libs": [],
        "x": 450,
        "y": 80,
        "wires": [
            [
                "8e11ed2178ace305"
            ]
        ]
    },
    {
        "id": "8e11ed2178ace305",
        "type": "ui_gauge",
        "z": "931153a67f419cc7",
        "name": "",
        "group": "04aec9e1fb3d61bc",
        "order": 0,
        "width": 0,
        "height": 0,
        "gtype": "gage",
        "title": "Temperature",
        "label": "C",
        "format": "{{value}}",
        "min": 0,
        "max": "100",
        "colors": [
            "#00b500",
            "#e6e600",
            "#ca3838"
        ],
        "seg1": "",
        "seg2": "",
        "className": "",
        "x": 750,
        "y": 80,
        "wires": []
    },
    {
        "id": "12731096ae105ada",
        "type": "function",
        "z": "931153a67f419cc7",
        "name": "Humidity node",
        "func": "msg.payload = msg.payload.Humidity\nglobal.set('h', msg.payload)\nreturn msg;",
        "outputs": 1,
        "noerr": 0,
        "initialize": "",
        "finalize": "",
        "libs": [],
        "x": 440,
        "y": 140,
        "wires": [
            [
                "ff717bcd6da128c5"
            ]
        ]
    },
    {
        "id": "ff717bcd6da128c5",
        "type": "ui_gauge",
        "z": "931153a67f419cc7",
        "name": "",
        "group": "04aec9e1fb3d61bc",
        "order": 0,
        "width": 0,
        "height": 0,
        "gtype": "gage",
        "title": "Humidity",
        "label": "%",
        "format": "{{value}}",
        "min": 0,
        "max": "100",
        "colors": [
            "#00b500",
            "#e6e600",
            "#ca3838"
        ],
        "seg1": "",
        "seg2": "",
        "className": "",
        "x": 740,
        "y": 140,
        "wires": []
    },
    {
        "id": "df8c8177c6f9b809",
        "type": "ui_button",
        "z": "931153a67f419cc7",
        "name": "",
        "group": "04aec9e1fb3d61bc",
        "order": 2,
        "width": 0,
        "height": 0,
        "passthru": false,
        "label": "Light ON",
        "tooltip": "",
        "color": "",
        "bgcolor": "",
        "className": "",
        "icon": "",
        "payload": "{\"command\":\"Light ON\"}",
        "payloadType": "json",
        "topic": "topic",
        "topicType": "msg",
        "x": 100,
        "y": 260,
        "wires": [
            [
                "e17f84198e248fc6",
                "685020225491f9c8"
            ]
        ]
    },
    {
        "id": "e17f84198e248fc6",
        "type": "debug",
        "z": "931153a67f419cc7",
        "name": "",
        "active": false,
        "tosidebar": true,
        "console": false,
        "tostatus": false,
        "complete": "payload",
        "targetType": "msg",
        "statusVal": "",
        "statusType": "auto",
        "x": 750,
        "y": 260,
        "wires": []
    },
    {
        "id": "35cb4c9b327d9cc2",
        "type": "ui_button",
        "z": "931153a67f419cc7",
        "name": "",
        "group": "04aec9e1fb3d61bc",
        "order": 3,
        "width": 0,
        "height": 0,
        "passthru": false,
        "label": "Light OFF",
        "tooltip": "",
        "color": "",
        "bgcolor": "",
        "className": "",
        "icon": "",
        "payload": "{\"command\":\"Light OFF\"}",
        "payloadType": "json",
        "topic": "topic",
        "topicType": "msg",
        "x": 100,
        "y": 320,
        "wires": [
            [
                "e17f84198e248fc6",
                "685020225491f9c8"
            ]
        ]
    },
    {
        "id": "685020225491f9c8",
        "type": "ibmiot out",
        "z": "931153a67f419cc7",
        "authentication": "apiKey",
        "apiKey": "b2ede069630b4886",
        "outputType": "cmd",
        "deviceId": "DeviceID1",
        "deviceType": "Devicetype1",
        "eventCommandType": "command",
        "format": "String",
        "data": "1",
        "qos": 0,
        "name": "IBM IoT",
        "service": "registered",
        "x": 740,
        "y": 320,
        "wires": []
    },
    {
        "id": "a9534596929fcd98",
        "type": "http in",
        "z": "931153a67f419cc7",
        "name": "",
        "url": "/sensor",
        "method": "get",
        "upload": false,
        "swaggerDoc": "",
        "x": 110,
        "y": 200,
        "wires": [
            [
                "7cd4e3e3f0b06bf6"
            ]
        ]
    },
    {
        "id": "13c73a4f8f26302d",
        "type": "http response",
        "z": "931153a67f419cc7",
        "name": "",
        "statusCode": "",
        "headers": {},
        "x": 730,
        "y": 200,
        "wires": []
    },
    {
        "id": "7cd4e3e3f0b06bf6",
        "type": "function",
        "z": "931153a67f419cc7",
        "name": "httpfunctionnode",
        "func": "msg.payload = { \"Temperature\": global.get(\"t\"), \"Humidity\": global.get(\"h\") }\nreturn msg;",
        "outputs": 1,
        "noerr": 0,
        "initialize": "",
        "finalize": "",
        "libs": [],
        "x": 430,
        "y": 200,
        "wires": [
            [
                "13c73a4f8f26302d"
            ]
        ]
    },
    {
        "id": "fd5239f9a0681d1f",
        "type": "http in",
        "z": "931153a67f419cc7",
        "name": "",
        "url": "/control",
        "method": "get",
        "upload": false,
        "swaggerDoc": "",
        "x": 110,
        "y": 380,
        "wires": [
            [
                "f1ebac02e2968dd6"
            ]
        ]
    },
    {
        "id": "88109f6551c2547c",
        "type": "http response",
        "z": "931153a67f419cc7",
        "name": "",
        "statusCode": "",
        "headers": {},
        "x": 730,
        "y": 380,
        "wires": []
    },
    {
        "id": "f1ebac02e2968dd6",
        "type": "function",
        "z": "931153a67f419cc7",
        "name": "command function node",
        "func": "msg.payload=msg.payload.command\nreturn msg;",
        "outputs": 1,
        "noerr": 0,
        "initialize": "",
        "finalize": "",
        "libs": [],
        "x": 450,
        "y": 380,
        "wires": [
            [
                "88109f6551c2547c",
                "e17f84198e248fc6",
                "685020225491f9c8"
            ]
        ]
    },
    {
        "id": "b2ede069630b4886",
        "type": "ibmiot",
        "name": "",
        "keepalive": "60",
        "serverName": "",
        "cleansession": true,
        "appId": "",
        "shared": false
    },
    {
        "id": "04aec9e1fb3d61bc",
        "type": "ui_group",
        "name": "Weather Monitoring",
        "tab": "c784f3676be6e912",
        "order": 1,
        "disp": true,
        "width": "6",
        "collapse": false,
        "className": ""
    },
    {
        "id": "c784f3676be6e912",
        "type": "ui_tab",
        "name": "Control",
        "icon": "dashboard",
        "disabled": false,
        "hidden": false
    }
]
