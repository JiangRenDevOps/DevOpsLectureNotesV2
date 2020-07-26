# Description

This is a brief guideline on setting up CI/CD for our CMS project.

# Tasks

## Task #1: Run a Jenkins in Kubernetes Cluster

## Task #2: Install Kubernetes plugin and configure Kubernetes in Jenkins
```
jenkins-1-jenkins-agents-connector:50000
```
![Alt text](images/CI_CD_CMS_02.png?raw=true)


https://github.com/jenkinsci/kubernetes-plugin/blob/master/README.md

Test your connection with a new test pipeline 
```
podTemplate {
    node(POD_LABEL) {
        stage('Run shell') {
            sh 'echo hello world'
        }
    }
}
```
![Alt text](images/CI_CD_CMS_05.png?raw=true)
![Alt text](images/CI_CD_CMS_04.png?raw=true)
You should see test pipeline running in a newly generated pod
![Alt text](images/CI_CD_CMS_06.png?raw=true)


## Task #3: Configure Credentials for Jenkins pipeline
Sample project: https://github.com/JiangRenDevOps/jrcms




## Task #4: Create Elastic Beanstalk environments in AWS
Create beanstock environments in aws:

![Alt text](images/CI_CD_CMS_03.png?raw=true)
![Alt text](images/CI_CD_CMS_07.png?raw=true)
![Alt text](images/CI_CD_CMS_08.png?raw=true)
![Alt text](images/CI_CD_CMS_09.png?raw=true)
![Alt text](images/CI_CD_CMS_10.png?raw=true)
![Alt text](images/CI_CD_CMS_11.png?raw=true)
![Alt text](images/CI_CD_CMS_12.png?raw=true)
![Alt text](images/CI_CD_CMS_13.png?raw=true)
![Alt text](images/CI_CD_CMS_14.png?raw=true)

You will need to update the `Jenkinsfile` and files under `deployment` folder accordingly.

## Task #5: Setup Github integration
https://github.com/JiangRenDevOps/DevOpsLectureNotesV2/tree/master/WK8_CI-CD-Jekins/4.Integrate-with-Github-Org

## Task #6: Play around
Make changes and test the auto deployment
