# Websocket Endpoints

This document describes the available websocket endpoints for the old panda (not FR3) and their example payloads or responses.

---

## Admin API

### `wss://172.16.0.2/admin/api/processes`
- **Description:** Returns the status of admin processes. 
- **Frequency:** 1 message per second
- **Example output:**
  ```
  "Up"
  ```

### `wss://172.16.0.2/admin/api/control-token`
- **Description:** Control token endpoint.

### `wss://172.16.0.2/admin/api/startup-phase`
- **Description:** Startup phase endpoint.

### `wss://172.16.0.2/admin/api/end-effector`
- **Description:** End effector configuration endpoint.

---

## Desk API

### `wss://172.16.0.2/desk/api/robot/configuration`
- **Description:** Provides robot configuration.
- **Frequency:** ~10 messages per second
- **Example output:**
  ```json
    {
        "estimatedForces": [
            -1.471145602911359,
            0.09145274113293178,
            2.176026845497451,
            -0.31509772026611504,
            0.5395616040828519,
            -0.15709500133021445
        ],
        "jointAngles": [
            -1.0198310156624033,
            -1.5261092590698617,
            -0.6334500071052738,
            -2.841345689483553,
            -0.14809008567698545,
            2.109184658523543,
            -0.040361572397227416
        ],
        "estimatedTorques": [
            0.04876286647769063,
            0.174641331048801,
            -0.27340239446784115,
            -0.7162828298501059,
            -0.2117492640486108,
            0.1248784199204833,
            -0.11614992209383077
        ],
        "cartesianPose": [
            0.6069055984094179,
            -0.23836713069824345,
            0.7581737614315078,
            0,
            -0.498561548246809,
            -0.8570969905452362,
            0.1296220595008894,
            0,
            0.6189427274003604,
            -0.45667343030651697,
            -0.6390299509806108,
            0,
            0.06716417693274476,
            -0.3206671200192838,
            0.41800010803372656,
            1
        ]
    }
  ```

### `wss://172.16.0.2/desk/api/robot/gripper_state`
- **Description:** Returns the current state of the gripper.
- **Frequency:** ~15 messages per second
- **Example output:**
  ```json
  {
    "width": -0.00000788000033935532,
    "maxWidth": 0
  }
  ```

### `wss://172.16.0.2/desk/api/robot/status`
- **Description:** Returns the robot's status.
- **Frequency:** ~1 message per second
- **Example output:**
  ```json
  {
	"recoveryMode": {
		"automatic": false,
		"folded": false
	},
	"robotErrors": {
		"startElbowSignInconsistent": false,
		"cartesianReflex": false,
		"cartesianPositionViolation": false,
		"instabilityDetected": false,
		"jointMoveInWrongDirection": false,
		"maxPathDeviationViolation": false,
		"forceControlSafetyLimitViolation": false,
		"cartesianVelocityViolation": false,
		"tauJRangeViolation": false,
		"baseAccelerationInitializationTimeout": false,
		"baseAccelerationInvalidReading": false,
		"forceControllerDesiredForceToleranceViolation": false,
		"jointP2PPlanningInsufficientTorque": false,
		"jointReflex": false,
		"jointPositionViolation": false,
		"selfCollisionViolation": false,
		"jointVelocityViolation": false,
		"cartesianVelocityProfileSafetyLimitViolation": false,
		"maxGoalPoseDeviationViolation": false
	},
	"endEffectorConfiguration": {
		"mass": 1,
		"inertia": [
			0.0010000000474974513,
			0,
			0,
			0,
			0.0024999999441206455,
			0,
			0,
			0,
			0.0017000000225380063
		],
		"centerOfMass": [
			-0.014999999664723873,
			0,
			0.029999999329447746
		],
		"transformation": [
			0.707099974155426,
			-0.707099974155426,
			0,
			0,
			0.707099974155426,
			0.707099974155426,
			0,
			0,
			0,
			0,
			1,
			0,
			0,
			0,
			0.188400000333786,
			1
		]
	},
  }
  ```

### `wss://172.16.0.2/desk/api/robot/guiding/mode`
- **Description:** Robot guiding mode.

### `wss://172.16.0.2/desk/api/robot/guiding/configuration`
- **Description:** Robot guiding configuration.
- **Example output:**
  ```json
  {
    "rotation_z": true,
    "translation_z": true,
    "translation_y": true,
    "translation_x": true,
    "elbow": false,
    "rotation_x": false,
    "rotation_y": false
  }
  ```

### `wss://172.16.0.2/desk/api/notification`
- **Description:** Notification endpoint.
- **Example output:** _No example available._

### `wss://172.16.0.2/desk/api/execution`
- **Description:** Execution endpoint.

### `wss://172.16.0.2/desk/api/skills`
- **Description:** Not Sure.

### `wss://172.16.0.2/desk/api/groups`
- **Description:** Not Sure.

### `wss://172.16.0.2/desk/api/timelines`
- **Description:** Not Sure.

### `wss://172.16.0.2/desk/api/timelines/{timeline_id}`
- **Description:** Returns a specific timeline.

### `wss://172.16.0.2/desk/api/navigation/mode`
- **Description:** Navigation mode endpoint.

### `wss://172.16.0.2/desk/api/navigation/events`
- **Description:** State of the keys on the robot. Not all keys may be present in the response. Only the initial message has all of them.
- **Trigger:** Triggered when button is pressed and on websocket creation.
- **Example output:**
  ```json
  {
    "check": false,
    "circle": false,
    "cross": false,
    "down": false,
    "left": false,
    "right": false,
    "up": false
  }
  ```

### `wss://172.16.0.2/desk/api/pilot/hardware`
- **Description:** Pilot hardware connection status.
- **Frequency:** ~0.5 messages per second
- **Example output:**
  ```json
  {
    "connectionStatus": "connected"
  }
  ```

### `wss://172.16.0.2/desk/api/base-leds/hardware`
- **Description:** Base LEDs hardware connection status.
- **Frequency:** ~0.5 messages per second
- **Example output:**
  ```json
  {
    "connectionStatus": "connected"
  }
  ```

### `wss://172.16.0.2/desk/api/events/gripper/hardware`
- **Description:** Gripper hardware events.
- **Frequency:** ~1 message per second
- **Example output:**
  ```json
  {
    "connection_status": "uninitialized"
  }
  ```

### `wss://172.16.0.2/desk/api/system/status`
- **Description:** System status.
- **Frequency:** ~2 message per second
- **Example output:**
  ```json
  {
    "ethernetConnected": true,
    "slavesOperational": true,
    "x3Enabled": false,
    "operationalMode": "SS1",
    "firmwareVersion": [
		"1.3.4-F-AX",
		"1.3.4-F-AX",
		"1.3.4-F-AX",
		"1.3.4-F-AX",
		"1.3.4-F-AX",
		"1.3.4-F-AX",
		"1.3.4-F-A7"
	],
	"lifetimePercentages": [
		0.604,
		300.067,
		1.392,
		49.714,
		0.001,
		47.334,
		0
	],
    "jointsInError": false,
    "x4Enabled": false,
    "startedWithEni": true,
    "connectedSlaves": 7,
    "masterStatus": "OP",
    "operationalModeTransitionReason": "NOMINAL",
    "brakesOpen": [ false, false, false, false, false, false, false ],
    "shutdownDataError": [ false, false, false, false, false, false, false ]
  }
  ```

---

## Notes

- For detailed skill and timeline structures, see the respective documentation.
- Example payloads are truncated for brevity.
- Replace `{timeline_id}` with the actual timeline identifier.

