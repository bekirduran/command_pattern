# Simple Command Pattern Example
### Command pattern turns a request into stand-alone object that containts all information about the request.This transformation lets you pass requests as a method arguments, delay or queue a request’s execution, and support undoable operations.

### Command objects serve as links between various GUI and business logic objects. the GUI object doesn’t need to know what business logic object will receive the request and how it’ll be processed. The GUI object just triggers the command, which handles all the details.

### Command(Maintenance) Abstraction Class is
<img src=command_pattern/ScreenShots/ss6.png width="600" height="250" >

### Command(Maintenance) implemented to MercedesMaintenance Class
<img src=command_pattern/ScreenShots/ss5.png width="580" height="180" >

### Command(Maintenance) implemented to BMWMaintenance Class
<img src=command_pattern/ScreenShots/ss3.png width="540" height="255" >

### Command(Maintenance) implemented to AudiMaintenance Class
<img src=command_pattern/ScreenShots/ss4.png width="530" height="180" >


### When the calling invoker and commands on main class:
<img src=command_pattern/ScreenShots/ss2.png width="725" height="437" >

### Then finally output is:
<img src=command_pattern/ScreenShots/ss1.png width="457" height="380" >


### with the help of Command Pattern, you can follow Single Responsibility Principle, Open/Closed Principle and You can assemble a set of simple commands into a complex one.
