# robosoccer_world_model
Maintains a full map of the field, ball, players

### Publishes
* `String`: `/world_state`: Environment

### Subscribes to
* `PoseStamped`: `/ball_pose`: Position of the ball
* `PoseStamped`: `/robot_pose`: Position of the robot
