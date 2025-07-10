# Websocket Endpoints

This document describes the available websocket endpoints on the panda platform, with notes on which are available for Panda, FR3, or both.

---

## Endpoint Availability by Platform

| Endpoint                                      | Panda | FR3  | Notes                                  |
|-----------------------------------------------|:-----:|:----:|----------------------------------------|
| `/admin/api/processes`                        |  ✔️   |  ✔️  |                                        |
| `/admin/api/control-token`                    |  ✔️   |  ✔️  |                                        |
| `/admin/api/startup-phase`                    |  ✔️   |  ✔️  |                                        |
| `/admin/api/end-effector`                     |  ✔️   |  ✔️  |                                        |
| `/admin/api/safety/status`                    |       |  ✔️  | FR3 only                               |
| `/admin/api/system-status`                    |       |  ✔️  | FR3 only                               |
| `/desk/api/robot/configuration`               |  ✔️   |  ✔️  |                                        |
| `/desk/api/robot/gripper_state`               |  ✔️   |  ✔️  |                                        |
| `/desk/api/robot/status`                      |  ✔️   |  ✔️  |                                        |
| `/desk/api/robot/guiding/mode`                |  ✔️   |  ✔️  |                                        |
| `/desk/api/robot/guiding/configuration`       |  ✔️   |  ✔️  |                                        |
| `/desk/api/notification`                      |  ✔️   |  ✔️  |                                        |
| `/desk/api/execution`                         |  ✔️   |  ✔️  |                                        |
| `/desk/api/skills`                            |  ✔️   |  ✔️  |                                        |
| `/desk/api/groups`                            |  ✔️   |  ✔️  |                                        |
| `/desk/api/timelines`                         |  ✔️   |  ✔️  |                                        |
| `/desk/api/timelines/{timeline_id}`           |  ✔️   |  ✔️  |                                        |
| `/desk/api/navigation/mode`                   |  ✔️   |  ✔️  |                                        |
| `/desk/api/navigation/events`                 |  ✔️   |  ✔️  | Button/key events                      |
| `/desk/api/pilot/hardware`                    |  ✔️   |  ✔️  |                                        |
| `/desk/api/base-leds/hardware`                |  ✔️   |  ✔️  |                                        |
| `/desk/api/events/gripper/hardware`           |  ✔️   |  ✔️  |                                        |
| `/desk/api/system/status`                     |  ✔️   |  ✔️  |                                        |
| `/admin/api/login`                            |  ✔️   |  ✔️  | **HTTP endpoint**                      |
| `/admin/api/logout`                           |  ✔️   |  ✔️  | **HTTP endpoint**                      |
| `/desk/api/operating-mode/execution`          |       |  ✔️  | **HTTP endpoint, FR3 only**            |
| `/desk/api/operating-mode/programming`        |       |  ✔️  | **HTTP endpoint, FR3 only**            |
| `/desk/api/robot/close-brakes`                |  ✔️   |      | **HTTP endpoint, Panda only**          |
| `/desk/api/robot/open-brakes`                 |  ✔️   |      | **HTTP endpoint, Panda only**          |
| `/desk/api/joints/lock`                       |       |  ✔️  | **HTTP endpoint, FR3 only**            |
| `/desk/api/joints/unlock`                     |       |  ✔️  | **HTTP endpoint, FR3 only**            |
| `/admin/api/reboot`                           |  ✔️   |  ✔️  | **HTTP endpoint**                      |
| `/admin/api/control-token/request`            |  ✔️   |  ✔️  | **HTTP endpoint**                      |
| `/admin/api/control-token/fci`                |  ✔️   |  ✔️  | **HTTP endpoint**                      |
| `/admin/api/control-token/fci` (DELETE)       |  ✔️   |  ✔️  | **HTTP endpoint**                      |

---

## HTTP Endpoints (not websockets)

### `POST /admin/api/login`
- **Platforms:** Panda, FR3
- **Description:** Login endpoint. Used to authenticate and obtain a session token.
- **Request body:**
  ```json
  {
    "login": "<username>",
    "password": "<encoded_password>"
  }
  ```
- **Response:** Session token (string).

### `POST /admin/api/logout`
- **Platforms:** Panda, FR3
- **Description:** Logout endpoint. Ends the current session.

### `POST /desk/api/operating-mode/execution`
- **Platforms:** FR3 only
- **Description:** Switches the robot to execution mode.

### `POST /desk/api/operating-mode/programming`
- **Platforms:** FR3 only
- **Description:** Switches the robot to programming mode. 

### `POST /desk/api/robot/close-brakes`
- **Platforms:** Panda only
- **Description:** Locks the brakes.

### `POST /desk/api/robot/open-brakes`
- **Platforms:** Panda only
- **Description:** Unlocks the brakes.

### `POST /desk/api/joints/lock`
- **Platforms:** FR3 only
- **Description:** Locks the brakes.

### `POST /desk/api/joints/unlock`
- **Platforms:** FR3 only
- **Description:** Unlocks the brakes.

### `POST /admin/api/reboot`
- **Platforms:** Panda, FR3
- **Description:** Reboots the robot hardware.

### `POST /admin/api/control-token/request`
- **Platforms:** Panda, FR3
- **Description:** Requests control of the Desk (optionally with `?force`).

### `POST /admin/api/control-token/fci`
- **Platforms:** Panda, FR3
- **Description:** Activates the Franka Research Interface (FCI).

### `DELETE /admin/api/control-token/fci`
- **Platforms:** Panda, FR3
- **Description:** Deactivates the Franka Research Interface (FCI).

---

## Admin API

### `wss://<host>/admin/api/processes`
- **Platforms:** Panda, FR3
- **Description:** Returns the status of admin processes.
- **Frequency:** 1 message per second
- **Example output:**
  ```
  "Up"
  ```

### `wss://<host>/admin/api/control-token`
- **Platforms:** Panda, FR3
- **Description:** Control token endpoint.

### `wss://<host>/admin/api/startup-phase`
- **Platforms:** Panda, FR3
- **Description:** Startup phase endpoint.

### `wss://<host>/admin/api/end-effector`
- **Platforms:** Panda, FR3
- **Description:** End effector configuration endpoint.

### `wss://<host>/admin/api/safety/status`
- **Platforms:** **FR3 only**
- **Description:** Safety status for FR3.
- **Example output:**
  ```json
     {
            "sequenceNumber": 18471788,
            "safetyControllerStatus": "Idle",
            "brakeState": [
                "Locked",
                "Locked",
                "Locked",
                "Locked",
                "Locked",
                "Locked",
                "Locked"
            ],
            "stoState": "SafeTorqueOff",
            "timeToTd2": 8252,
            "activeWarnings": {
                "safetySettingsInvalidated": false,
                "temperatureHigh": false
            },
            "demandedRecoveries": {
                "jointLimitViolation": [
                    false,
                    false,
                    false,
                    false,
                    false,
                    false,
                    false
                ],
                "jointPositionError": [
                    false,
                    false,
                    false,
                    false,
                    false,
                    false,
                    false
                ],
                "safetyRuleViolationsConfirmation": {},
                "safetyRuleViolationsRecovery": {}
            },
            "recoverableErrors": {
                "environmentDataTimeout": false,
                "fsoeConnectionError": false,
                "genericJointError": false,
                "guidingEnablingDevice": false,
                "jointPositionError": false,
                "safeInputErrorX31": false,
                "safeInputErrorX32": false,
                "safeInputErrorX33": false,
                "safeInputErrorX4": false,
                "td2Timeout": false
            },
            "activeRecovery": null,
            "safeInputState": {
                "guidingEnableButton": "Inactive",
                "x31": "Active",
                "x32": "Inactive",
                "x33": "Inactive",
                "x4": "Inactive"
            },
            "powerState": {
                "endEffector": "Off",
                "robot": "On"
            },
            "safetyControllerStatusReason": {
                "conflictingInputs": false,
                "fsoeWatchdogError": false,
                "sacoVersionMismatch": false,
                "nonRecoverableSafetyError": false,
                "temperatureError": false,
                "connectionToSafetySettingsManagerLost": false,
                "environmentDataMissing": false,
                "jointsSafetyError": [
                    false,
                    false,
                    false,
                    false,
                    false,
                    false,
                    false
                ],
                "safetyVersionMismatch": false
            },
            "safetyConfigurationIndex": 0,
            "fsoeConnectionStatus": [
                "Data",
                "Data",
                "Data",
                "Data",
                "Data",
                "Data",
                "Data"
            ]
        }
    ```

### `wss://<host>/admin/api/system-status`
- **Platforms:** **FR3 only**
- **Example output:**
  ```json
   {
      "execution": {
          "aborted": false,
          "error": null,
          "errorHandling": false,
          "lastActivePath": null,
          "remainingWaitTime": null,
          "running": false,
          "state": {
              "active": false,
              "children": [],
              "exitPort": null,
              "id": null,
              "result": null
          },
          "tracking": true
      },
      "safety": {
          "sequenceNumber": 18487175,
          "safetyControllerStatus": "Idle",
          "brakeState": [
              "Locked", # "Locked" or "Unlocked"
              "Locked",
              "Locked",
              "Locked",
              "Locked",
              "Locked",
              "Locked"
          ],
          "stoState": "SafeTorqueOff",
          "timeToTd2": 8101,
          "activeWarnings": {
              "safetySettingsInvalidated": false,
              "temperatureHigh": false
          },
          "demandedRecoveries": {
              "jointLimitViolation": [
                  false,
                  false,
                  false,
                  false,
                  false,
                  false,
                  false
              ],
              "jointPositionError": [
                  false,
                  false,
                  false,
                  false,
                  false,
                  false,
                  false
              ],
              "safetyRuleViolationsConfirmation": {},
              "safetyRuleViolationsRecovery": {}
          },
          "recoverableErrors": {
              "environmentDataTimeout": false,
              "fsoeConnectionError": false,
              "genericJointError": false,
              "guidingEnablingDevice": false,
              "jointPositionError": false,
              "safeInputErrorX31": false,
              "safeInputErrorX32": false,
              "safeInputErrorX33": false,
              "safeInputErrorX4": false,
              "td2Timeout": false
          },
          "activeRecovery": null,
          "safeInputState": {
              "guidingEnableButton": "Inactive",
              "x31": "Active",
              "x32": "Inactive",
              "x33": "Inactive",
              "x4": "Inactive"
          },
          "powerState": {
              "endEffector": "Off",
              "robot": "On"
          },
          "safetyControllerStatusReason": {
              "conflictingInputs": false,
              "fsoeWatchdogError": false,
              "sacoVersionMismatch": false,
              "nonRecoverableSafetyError": false,
              "temperatureError": false,
              "connectionToSafetySettingsManagerLost": false,
              "environmentDataMissing": false,
              "jointsSafetyError": [
                  false,
                  false,
                  false,
                  false,
                  false,
                  false,
                  false
              ],
              "safetyVersionMismatch": false
          },
          "safetyConfigurationIndex": 0,
          "fsoeConnectionStatus": [
              "Data",
              "Data",
              "Data",
              "Data",
              "Data",
              "Data",
              "Data"
          ]
      },
      "robot": {
          "closeToSingularity": false,
          "endEffectorConfiguration": {
              "centerOfMass": [
                  -0.009999999776482582,
                  0,
                  0.029999999329447746
              ],
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
              "mass": 0.7300000190734863,
              "transformation": [
                  0.7071067690849304,
                  -0.7071067690849304,
                  0,
                  0,
                  0.7071067690849304,
                  0.7071067690849304,
                  0,
                  0,
                  0,
                  0,
                  1,
                  0,
                  0,
                  0,
                  0.10339999943971634,
                  1
              ]
          },
          "robotErrors": []
      },
      "processes": "Up",
      "startup": {
          "tag": "Started"
      },
      "controlToken": {
          "activeToken": {
              "id": 645396955,
              "ownedBy": "admin"
          },
          "fciActive": false,
          "tokenRequest": null
      },
      "derived": {
          "operatingMode": "Programming",
          "desiredColor": {
              "color": "Blue",
              "mode": "Constant"
          },
          "td2Tests": {
              "status": "OK",
              "canExecute": true
          },
          "lifetime": {
              "status": "OK",
              "lifetime": 0.013,
              "isConfirmationNeeded": false
          }
      }
        
  }
  ```


---

## Desk API

### `wss://<host>/desk/api/robot/configuration`
- **Platforms:** Panda, FR3
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

### `wss://<host>/desk/api/robot/gripper_state`
- **Platforms:** Panda, FR3
- **Description:** Returns the current state of the gripper.
- **Frequency:** ~15 messages per second
- **Example output:**
  ```json
  {
    "width": -0.00000788000033935532,
    "maxWidth": 0
  }
  ```

### `wss://<host>/desk/api/robot/status`
- **Platforms:** Panda, FR3
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

### `wss://<host>/desk/api/robot/guiding/configuration`
- **Platforms:** Panda, FR3
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

### `wss://<host>/desk/api/notification`
- **Platforms:** Panda, FR3
- **Description:** Notification endpoint.

### `wss://<host>/desk/api/execution`
- **Platforms:** Panda, FR3
- **Description:** Execution endpoint.

### `wss://<host>/desk/api/skills`
- **Platforms:** Panda, FR3
- **Description:** Returns available robot skills.

### `wss://<host>/desk/api/groups`
- **Platforms:** Panda, FR3
- **Description:** Groups endpoint.

### `wss://<host>/desk/api/timelines`
- **Platforms:** Panda, FR3
- **Description:** Returns available timelines.

### `wss://<host>/desk/api/timelines/{timeline_id}`
- **Platforms:** Panda, FR3
- **Description:** Returns a specific timeline.

### `wss://<host>/desk/api/navigation/mode`
- **Platforms:** Panda, FR3
- **Description:** Navigation mode endpoint.

### `wss://<host>/desk/api/navigation/events`
- **Platforms:** Panda, FR3
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

### `wss://<host>/desk/api/pilot/hardware`
- **Platforms:** Panda, FR3
- **Description:** Pilot hardware connection status.
- **Frequency:** ~0.5 messages per second
- **Example output:**
  ```json
  {
    "connectionStatus": "connected"
  }
  ```

### `wss://<host>/desk/api/base-leds/hardware`
- **Platforms:** Panda, FR3
- **Description:** Base LEDs hardware connection status.
- **Frequency:** ~0.5 messages per second
- **Example output:**
  ```json
  {
    "connectionStatus": "connected"
  }
  ```

### `wss://<host>/desk/api/events/gripper/hardware`
- **Platforms:** Panda, FR3
- **Description:** Gripper hardware status.
- **Frequency:** ~1 message per second
- **Example output:**
  ```json
  {
    "connection_status": "uninitialized"
  }
  ```

### `wss://<host>/desk/api/system/status`
- **Platforms:** Panda, FR3 (Outputs are different)
- **Description:** System status.
- **Frequency:** ~2 messages per second
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

  - **Example FR3 output:**
  ```json
        {
            "connectedSlaves": 7,
            "ethernetConnected": true,
            "firmwareDownloadStatus": [
                "INITIAL_STATE",
                "INITIAL_STATE",
                "INITIAL_STATE",
                "INITIAL_STATE",
                "INITIAL_STATE",
                "INITIAL_STATE",
                "INITIAL_STATE"
            ],
            "firmwareVersion": [
                "2.0.7-F",
                "2.0.7-F",
                "2.0.7-F",
                "2.0.7-F",
                "2.0.7-F",
                "2.0.7-F",
                "2.0.7-F"
            ],
            "jointStatus": [
                0,
                0,
                0,
                0,
                0,
                0,
                0
            ],
            "jointsInError": false,
            "lifetimeConfirmationNeeded": false,
            "lifetimePercentages": [
                0,
                0.013,
                0,
                0.001,
                0,
                0,
                0
            ],
            "masterStatus": "OP",
            "slavesOperational": true,
            "startedWithEni": true
        }
  ```