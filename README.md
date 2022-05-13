# Table of contents
- [Overview](#overview)
- [Arquitecture and methodology](#arquitecture-and-methodology)
  - [Reading of the txt file](#reading-of-the-txt-file)
  - [Convertion of time format](#convertion-of-time-format)
  - [Computation of the value of hours and worked hours](#computation-of-the-value-of-hours-and-worked-hours)
  - [Main function](#main-function)
- [How to run](#how-to-run)

# Overview
This is a solution for ioet coding test where we needed to calculate the employee pay based on hours and days worked. In addition, a "txt" file containing the inputs to work with is included in this repository. At least 5 sets of inputs were included.

To consider a valid input the structure has to be the following: 

RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00

Here we can see that input contains the name of an employee and the schedule they worked being:

- MO: Monday

- TU: Tuesday

- WE: Wednesday

- TH: Thursday

- FR: Friday

- SA: Saturday

- SU: Sunday

Regarding to the working hours it's needed to select one of the valid schedules without combine hours. 

The available schedules and the pay per hour are the following:

Monday - Friday

- 00:01 - 09:00 25 USD

- 09:01 - 18:00 15 USD

- 18:01 - 00:00 20 USD

Saturday and Sunday

- 00:01 - 09:00 30 USD

- 09:01 - 18:00 20 USD

- 18:01 - 00:00 25 USD

To add new data has to be in a new line inside of txt file like the following example:

RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00 <br />
ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00

After the running of the program the output will be printed being the following:

OUTPUT<br />
The amount to pay RENE is: 215.0 USD<br />
The amount to pay ASTRID is: 85.0 USD

# Arquitecture and methodology
The structure of the code consist of the following parts:

## Reading of the txt file
This section allows you to read the txt file located inside the same folder.

## Conversion of time format 
Here a function called "time_to_decimal" make the task of convert the format time to decimal format, allowing the handle of the pay of fractions of hours.

## Computation of the value of hours and worked hours
In this section the function "val_hr" compute the value of the hour and the worked hours according to the schedule. If there's a merge in schedules an exception is excuted indicating in which part of the input is the problem.

## Main function
In the main function the input data is structure into a dictionary in which every employee has key/value pairs indicating the worked hours per day, the pay per day and the total pay. These elements are obtained by calling function like "val_hr" and "time_to_decimal". Finally the output of every employee is printed.

# How to run
To run the code is needed that input data is structure in a valid format mentioned in the [Overview](#overview) section. Also the "txt" file need to be in the same folder of code.
