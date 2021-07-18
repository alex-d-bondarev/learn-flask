# plan

Need to implement some generic functionality for test demo purposes. This functionality should:

1. Require DB integration :white_check_mark:
    1. Create docker-compose with mysql :white_check_mark:
    1. Add SQLAlchemy integration :white_check_mark:
1. Simulate CRUD for generic accounts :white_check_mark:
    1. Account should consist of: :white_check_mark:
        1. id
        1. name - for text update actions
        1. number - for number update actions
        1. role - for generic account roles
    1. Account data should be stored in DB :white_check_mark:
    1. Create CRUD API endpoint :white_check_mark:
1. _Simulate generic actions (do_something) against accounts combined with roles_
    1. _Create `do_something_public` endpoint:_
        1. _It can be used without restrictions._
        1. _No input parameters are required._
        1. _A full response is returned immediately._
    1. Create `do_something_private` endpoint: :white_check_mark:
        1. It can be used only by users and admins. :white_check_mark:
        1. Account name parameter as input. :white_check_mark:
        1. A short response with response ID is returned immediately. :white_check_mark:
        1. A full response with 'processing delay' is returned, when additional response ID is
           provided. :white_check_mark:
    1. _Create `do_something_admin` endpoint:_
        1. _Same as `do_something_private` but only for admins_
1. _Simulate CRUD for processing delays_ :hourglass_flowing_sand:
    1. _Simulate processing delays by adding delays to endpoints_
        1. Add max_delay value :white_check_mark:
        1. _Add random delay True|False_
            1. _If random delay is between 0 and max_delay_
            1. _Else delay is max_delay_
1. Use TDD :stuck_out_tongue_winking_eye:
1. Update this README to show progress:
    1. _Italics_ = TBD
    1. _Italics_ and :hourglass_flowing_sand: = In Progress
    1. Regular text and :white_check_mark: = Done
