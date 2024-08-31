Hi! Welcome to my public GitHub repository!

##########
About me:
I'm part of Dr. Richard Anantua's black hole research group. I am an undergraduate astrophysics major at the University of Texas at San Antonio (UTSA). I am also very new to Astrophysics and Python (really, its coding in general). For this current semester (Fall 2024), I'm taking Modern Physics, Math Physics, and Classical Mechanics, which are all pretty early physics classes. 

##########
My research:
I mainly work on creating black hole simulations of M87* using ipole (https://github.com/AFD-Illinois/ipole.git) and a few custom Python scripts created by my research group. The basic premise of our work is we know the observed outputs (flux, polarization, etc) of M87* from several papers published by EHT; we don't know the inputs that produced those outputs—the main input we are investigating is the Munit. In other words, we don't know the details of the process that created the telescope data we see for M87*.

A Munit is what I like to call a general-size unit that we use for GRMHD simulations of accreting systems—which are scale-invariant. So the Munit is a free parameter that scales the gas density of the systems.

##########
The current problem:
The current way of finding Munits is slow and impractical. It consists of trying an educated guess, running ipole on a high-performance computing cluster, compare the sim's output with an observed output (we normally use flux as the filter), and repeat if it doesn't match. It normally takes us an extremely long time to find the correct Munit, so I've been investigating the data analysis side of things and trying to incorporate machine learning and neural networks into our process of finding a correct Munit.

Another important note about how we input Munits is that we also try to take into account the positron ratio, which splits the Munit into two inputs that are run through the pole. The first input is a simulation with no positrons, and the second input is a simulation with the maximum amount of positrons for the Munit. So this splitting makes it exponentially harder as (1) it takes a few minutes per simulation, (2) most common search algorithms aren't easily applicable, and (3) both simulation outputs must make it past the filter (a target flux that rounds to .5 Jy) for the Munit used to be accepted.

We currently have an exponential search algorithm that theoretically could give us an array of possible Munits, but it (1) hasn't been tested yet, and (2) doesn't tell us what Munit has 0 positrons and what Munit has the maximum number of positrons.

##########
The current work history:
The script that considers the positron ratio has two inputs: MunitOffset and MunitSlope. MunitSlope will be divided by 1 and 3 respectively for the minimum and maximum Munit used in the simulation. The product of this equation is an array and is assigned to the variable MunitUsed, which is fed into ipole.

Now this is where my work I discussed earlier comes into play. 

Before we were given the exponential search algorithm, I had semi-automated the Munit finding process, where a queue is made through a grid of numbers or random numbers, both confined to a set range. The positron ratio script would pop the first entry in the queue and put the calculated MunitUsed array into ipole. After a minimum and maximum flux were produced for a queue entry, a bash script would save the inputs and outputs to a .JSON file named dataCollect.json and check if both calculated fluxes can round to .5 Jy. If the flux outputs don't pass the filter, it tries the next entry in the queue.

The problem with this method is that it is slow and not very smart. Also, despite a few hundred or so attempts recorded in dataCollect.json, no Munits were found using these methods.

After these initial algorithms, I had also realized the slowest factor was waiting ~5 minutes for ipole to run each simulation. There was also a problem where ipole would run entries in the queue that were already tried or were utterly unreasonable to try.

An important note is that MunitSlope seems to be in the magnitude of 10^5, and MunitOffset is in the magnitude of 10^15.

##########
The current work:
I began feeding the data collected into a random forest algorithm to predict the flux for a given MunitOffset and MunitSlope. The algorithm's estimated accuracy was low; however, in practice, when trying reasonable inputs, the algorithm could predict the correct flux output of ipole within around three decimal places. However, there were still no successful outputs that passed the filter of being able to round flux to .5 Jy.

Another random forest algorithm was created to predict which combination of MunitOffset and MunitSlope values would produce a flux that can round to .5 Jy. When tested, this script was unable to find a set of values. The code is still a work in progress, and I believe the problem may be with how it chooses random numbers. Since the numbers we are working with are so large, it's improbable to generate a number in the magnitude of <10^3 and extremely likely to choose a number in the magnitude of 10^18 due to the nature of how big these numbers are.

None of the random forest algorithms have been incorporated into the semi-automated Munit search process.

There are also plans to simplify the process by using some search algorithm purely on MunitUsed and not MunitOffset and MunitSlope. This is what the exponential search algorithm we received does. Then, once an array of possible MunitUsed values that pass the filter are found, some script would solve for the solution of the two missing variables.
