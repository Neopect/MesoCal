# MesoCal

MesoCal will be designed as a Macrocycle builder for scheduling and weight forecasting. The plan is to make it dynamic between custom mesocycles and adjust throughout your macrocycle.

## State

The state of this script/app is fundamental. I haven't spent much time expanding feature sets or making them more stable and user-friendly. It currently follows a strict process to function.


## How to use the application?

To run this script, you need to have 2 things ready, the script and your adequately formatted JSON file within your working directory. Then follow the following prompts:
1. Type 2 for `2. Build Macrocycle`
2. Type 1 for JSON
3. Type the assigned number for the designated file
4. Your output.csv file will be saved to your cwd

Everything else on this application so far are placeholders and/or don't serve any function at this time. They will be removed or built upon as time and progress permits.

## JSON formatting
I have provided a sample JSON file as an example of how to base custom macrocycles.

Here's the code snip-it:
```
{
    "name":"",
    "startDate":"1/1/25",
    "startingWeight":200,
    "cycleNumberPrefix":"",
    "mesocycles": [
        {"name": "", "weeks": 4, "deload": [4], "glmrStat": "", "rate":0.25},
        {"name": "", "weeks": 2, "deload": [], "glmrStat": "", "rate":0}
    ],
    "manualWeights": [
        {"week":2,"weight":205}
    ]
}
```

You can have as many mesocycles and manual weight entries as possible. Still, you need at least one mesocycle for the script to function. 

`startDate` - Represents start date for your Macrocycle (Must be a Monday for formatting reasons)

`startingWeight`- Your starting weight

`cycleNumberPrefix` - Mesocycles are numbered 1-9+. If you want to create a prefix like `1.`, it will output like `[1.1, 1.2, 1.3]`. This can be helpful for documentation reasons when you're storing multiple Macrocycles or variations of them to stay better organized.

`mesocycles` - List of your mesocycles

`{"name": "", "weeks": 4, "deload": [4], "glmrStat": "", "rate":0.25}`
- `name` is your meso's name
- `weeks` is how many total weeks within meso
- `deload` is a list of each deload week within your mesocycle. Each number on the list will be marked as a deload, so set your gain rate to 0 for that week. If your meso doesn't have a deload, you can leave it empty
- `glmrStat` is meant to represent the type of cycle, it serves no purpose atm and is WIP
- `rate` is your gain/lose rate for body weight. The number is taken as a percentage. In this example, `0.25` means you plan to gain 0.25% body weight per week


## Future Feature/Change Ideas
- Build a more stable interface
- More code formatting more consistent
- Be able to manually create macrocycles without json using prompts
- Multiple output formats (printf, markdown, pdf, xlsx)
- More manipulation and options in output
- Display Macrocycle Analytics 
