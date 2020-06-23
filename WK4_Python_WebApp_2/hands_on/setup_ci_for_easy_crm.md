
# A simple Travis hands on

Let us trigger the CI build for EasyCRM
 
#### 1. Fork EasyCRM to your own repo

click the fork button on https://github.com/JiangRenDevOps/EasyCRM

#### 2. Login to Travis

login to https://travis-ci.org/ with your github account

#### 3. Add the newly forked repo

Add the newly forked repo by click the + button 

![Alt text](../images/create_a_new_repo_on_travis.png?raw=true) 

and turn on CI for the repo that you just forked

![Alt text](../images/turn_on_ci.png?raw=true) 

Now, click the settings

#### 4. Manually trigger the EasyCRM master branch

Click on the dropdown and select the trigger build button
![Alt text](../images/trigger_build.png?raw=true) 

Choose the right branch, for now we only have a `master` branch
![Alt text](../images/trigger_build_select_branch.png?raw=true) 

A successful running CI would look like this 
![Alt text](../images/travis_ci_easycrm.png?raw=true) 

## Questions

Could you explain what is happening in the Job log?

What do you see when expanding line 1, 7, 164, 180?

How does the build know we exit correctly?

Looking back to .travis.yml file, could you easily tell what did we do and how to reproduce it locally?

## A short version of CI definition and what you can do with it

Continuous Integration is the practice of merging in small code changes frequently - 
rather than merging in a large change at the end of a development cycle. 
The goal is to build healthier software by developing and testing in smaller increments. 
This is where Travis CI comes in.

![Alt text](../images/simplified_ci_diagram.png?raw=true) 
 

![Alt text](../images/simple_ci.png?raw=true) 

As a continuous integration platform, Travis CI supports your development process by automatically building and testing code changes, providing immediate feedback on the success of the change. 
Travis CI can also automate other parts of your development process by managing deployments and notifications.

Travis CI is only one of many popular CI/CD platform. There are also many others available in the market: 
such as Bitbucket Pipeline, Bamboo, Jenkins etc..


## Some terms in Travis

* build - a group of jobs that run in sequence. For example, a build might have two jobs, each of which tests a project with a different version of a programming language. A build finishes when all of its jobs are finished.

* stage - a group of jobs that run in parallel as part of a sequential build process composed of multiple stages.

* job - an automated process that clones your repository into a virtual environment and then carries out a series of phases such as compiling your code, running tests, etc. A job fails, if the return code of the script phase is non-zero.

* phase - the sequential steps of a job. For example, the install phase, comes before the script phase, which comes before the optional deploy phase.


Could you identify build, job, phase in our EasyCRM example?

What is stage? https://docs.travis-ci.com/user/build-stages/

# Some other things that you may need to know

![Alt text](../images/ci_cd.png?raw=true)

Continuous Deployment

https://docs.travis-ci.com/user/deployment here is a list of supported providers and some type of deployment may not be suited