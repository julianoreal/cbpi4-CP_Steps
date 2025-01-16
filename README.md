# CBPi4 Plugin for Mash Steps Cervejaria Pederneiras

This plugin can be used as example for step plugins

## Several steps for CBPi4 that allow a full brewing
### These steps can be used to run a Speidel Braumeister automatically if the corresponding KettleLogic Plugin (cbpi4-_PIDSmartBoilWithPump) is also used

- CP_SpargeStep:
	- TODO
	- Parameters:
		- Temp: Target Temp for MashInStep
		- Sensor: Sensor to be used for this step
		- Kettle: Kettle to be used for this step
		- AutoMode: If yes: Kettle Logic will be switched on/off when step starts/stops

- CP_MashInStep:
	- Heats up to the target temp and stops when temp is reached. This can be used to add e.g. Malt Pipe. User has to manually move to next step
	- Parameters:
		- Temp: Target Temp for MashInStep
		- Sensor: Sensor to be used for this step
		- Kettle: Kettle to be used for this step
		- AutoMode: If yes: Kettle Logic will be switched on/off when step starts/stops

- CP_MashStep:
	- Heats up to the target temp and runs until Timer is done.
	- Parameters:
		- Time: Time in Minutes for Timer
		- Temp: Target Temp for MashStep
		- Sensor: Sensor to be used for this step
		- Kettle: Kettle to be used for this step
		- AutoMode: If yes: Kettle Logic will be switched on/off when step starts/stops

- CP_BoilStep:
	- Heats up to the target temp and runs until Timer is done. Is sending notifications to add hops
	- Parameters:
		- Time: Time in Minutes for Timer
		- Temp: Target Temp for BoilStep
		- Sensor: Sensor to be used for this step
		- Kettle: Kettle to be used for this step
		- AutoMode: If yes: Kettle Logic will be switched on/off when step starts/stops
		- First Wort: Sends a notification for First Wort Hops on Start if set to 'Yes'
		- Hop [1-6]: Sends up to 6 notifications for Hop alarms on specified times
			- Time is remaining Boil time in Minutes
		- Hop_text [1-6]: Name of Hops, additions (will be collected from BF, xml recipes,... in case of automated recipe creation)

- CP_Cooldown:
	- Waits that Wort is cooled down to target temp and is sending a notification. Active Step if Actor is selected.
	- Parameters:
		- Temp: Target Temp for Notification
		- Sensor: Sensor to be used for this step
		- Kettle: Kettle to be used for this step
		- Actor: Actor that is switched on during cooldown f selected (can be used to trigger a magnetic valve)
		- Interval: Interval in minutes when Step is checking current temp and calclulating estimated end time (2nd degree polynomial model)

- CP_SimpleStep:
	- Is sending a Notification and can wait on user
	- Parameters:
		- Notification: Notification text that can be specified by user
		- AutoNext: If set to 'No', step is wating for user input to move to next step. Otherwsie, next step is automatically started.

### Changelog:

- 08.01.25 (Still Beta Test)

- Added several steps
	- MashIn with Pause and request to add malt pipe before next step can be manually started
	- Mashout (SimpleStep) with Pause to remove Malt Pipe before boiling can be started -> Text Notificatrion to be set
	- Cooldown Step where Target temp can be set. Once temp is reached, notification is send
	- Modification of Voilstepd timer handling -> no mod of cbpi timer is required anymore