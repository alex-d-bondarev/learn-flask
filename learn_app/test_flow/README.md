# plan

Need to implement some generic functionality for test demo purposes. This
functionality should:

1. _Require DB integration_
    1. _Use docker_
    1. _No need to save data between sessions_
    1. _Create 'demo' record for each entity (bellow) during app start up_
1. _Simulate CRUD for generic accounts_
    1. _Account should consist of:_
        1. id
        1. name - for text update actions
        1. number - for number update actions
    1. _Account data should be stored in DB_
1. _Simulate CRUD for generic account roles_
    1. _Simulate admin with access to all endpoints_
    1. _Simulate user with limited access to endpoints_
1. _Simulate generic actions (do_something) against accounts combined with roles_
    1. _Create `do_something_public` endpoint:_
        1. _It can be used without restrictions._
        1. _No input parameters are required._
        1. _A full response is returned immediately._
    1. _Create `do_something_private` endpoint:_
        1. _It can be used only by users and admins._
        1. _Account id parameter as input._
        1. _A short response with response ID is returned immediately._
        1. _A full response with 'processing delay' is returned, when additional
           response ID is provided._
    1. _Create `do_something_admin` endpoint:_
        1. _Same as `do_something_private` but only for admins_
1. _Simulate CRUD for processing delays_
    1. _Simulate processing delays by adding delays to endpoints_
1. Use TDD :stuck_out_tongue_winking_eye:
1. Update this README to show progress:
    1. _Italics_ = TBD
    1. _Italics_ and :hourglass_flowing_sand: = In Progress
    1. Regular text and :white_check_mark: = Done
