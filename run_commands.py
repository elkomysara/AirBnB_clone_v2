
from console import HBNBCommand

# Create an instance of the command interpreter
cmd = HBNBCommand()

# Simulate the 'create' commands for State
cmd.onecmd('create State name="California"')
cmd.onecmd('create State name="Arizona"')

# Invoke the 'all' command to print all 'State' instances
cmd.onecmd('all State')

# Simulate the 'create' command for Place with parameters
cmd.onecmd('create Place city_id="0001" user_id="0001" name="My_little_house" number_rooms=4 number_bathrooms=2 max_guest=10 price_by_night=300 latitude=37.773972 longitude=-122.431297')

# Invoke the 'all' command to print all 'Place' instances
cmd.onecmd('all Place')
