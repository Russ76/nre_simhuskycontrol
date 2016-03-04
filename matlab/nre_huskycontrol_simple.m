% Necessary if not already done
%rosinit('127.0.0.1')

% Set waypoint for Husky to drive to
goal = [8,8];  % Goal position in x/y

% Setup publisher
cmdpub = rospublisher('/cmd_vel');
cmdmsg = rosmessage('geometry_msgs/Twist');

% Setup subscription - which implemets our controller.
% We pass the publisher, the message to publish and the goal as 
% additional parameters to the callback function.
odomsub = rossubscriber('/odom',{@huskyOdomCallback,cmdpub,cmdmsg,goal});



