# README

## Step 1: Go to the AWS Managment Console
Go to the [AWS Management Console](https://signin.aws.amazon.com/signin?redirect_uri=https%3A%2F%2Fconsole.aws.amazon.com%2Fconsole%2Fhome%3FhashArgs%3D%2523%26isauthcode%3Dtrue%26nc2%3Dh_ct%26src%3Dheader-signin%26state%3DhashArgsFromTB_us-east-2_25ae2f2047b54da9&client_id=arn%3Aaws%3Asignin%3A%3A%3Aconsole%2Fcanvas&forceMobileApp=0&code_challenge=FdLOpxhZeCFC6Ug37FJapg1uZQJ6TIV-g1nts4-2ElE&code_challenge_method=SHA-256) and log in to your AWS account. If you don't have one, create a new account.

Once you have logged into to the Management Console, look at the right most side of your screen. There should be your account name, and right next to it, it's a State. Click on that. Once you clicked on it, the first thing that pops up is your region in orange. To the right of that is your region name. Copy that name and write it down somewhere, you'll need it later.

After that, click on the search bar and type in "ecr". The first thing that pops up is "Elastic Container Registry". Click on that.

When you're in ECR, click the three bars on the panel on the left side. Look underneath Public Registry and click on Repositories. Click the orange button on the right that says, "Create repository". When creating your repository, MAKE SURE TO SELECT PUBLIC. The panel below that shows "Detail" Enter in any name for your Repository. After that scroll all the way down to the bottom and click "Create repository". Once it's been create, there's a column called "URI". Below that is the URI Link. Click the two squares of the left of the URI to copy the link and paste it somewhere. You'll need it soon. Once you're done with that open up the aws_ecr_launcher.sh file.

Once it's opened, change the IMG_NAME to whatever name you want. Make sure to replace it, IMG_NAME appears on the first and second lines. After that, replace the REGION_PLACE with the region name you copied earlier. Once you have replaced REGION_NAME, copy the URI link you have and paste it into the URI_LINK fields. It appears in the last 3 lines. Once you're done with that, save it and close it.

## Step 2: Uploading files to ECR
Open up your Terminal(Mac) or PowerShell(Windows). Go to the AWS_ECS folder. Once your there launch this script:

For Mac users type in either:
aws_ecs_launcher.sh
OR
./aws_ecs_launcher.sh

For Windows users type in:
.\ecr_win_launcher

Once you ran the script, return to the AWS console and go to ECR. Click on your repository. Inside your repository should be something called "latest".

## Step 3: Creating an ECS Cluster
After that, go to the search bar and search up ecs. Click on "Elastic Container Service". Click on the 3 bars on the left side and click on "Clusters". Click the orange button that says "Create cluster". When you're there, choose a cluster name, it can be anything you want. Right below that box should be an "Infrastucture" box. MAKE SURE THAT ONLY AMAZON EC2 INSTANCES HAS A CHECK MARK NEXT TO IT. After that, go to the next box that says "Network setting for Amazon EC2 Instances". Underneath "VPC", click on the first one. Underneath subnets, select all of them. Below that should be "Security group". Select "Use an existing security group". Underneath that should be a "Security group name". Click on the dropdown box and select the first one. After that, scroll to the bottom and click on the orange button that says "Create".

## Step 4: Creating a Task definition
Once you have finished creating your cluster, go to the left side of the screen and click on "Task definitions". Click on "Create new task definition" and select the FIRST OPTION. Once you are in the create menu, choose any name for your task definition. Go to the next box called "Infrasturcture requirements"and make sure that AMAZON EC2 INSTANCES HAVE A BLUE CHECKBOX. AWS FARGATE SHOULD BE UNSELECTED. Scroll down to "Network mode". Click on it and select "default". After that, scroll down to "Task size". Make sure that you have 1 vCPU and 0.5 GB ONLY. Scroll down to "Container" and give it a name. Copy the URI from before and paste it into "Image URI". After that go to "Port mappings" and click on "Container port". Make sure the port is 8501. Once you have down that, scroll all the way down and click on the orange "Create" button.

## Step 5: Creating Target Groups
Go to the search bar and type in "ec2". Click on the first option that says "EC2". On the left hand menu, scroll all the way down. Underneath "Load Balancing", which is the second to last dropdown box, select "Target Groups". Once you are in target groups, click the orange button that says "Create target group". When you are in the creation menu, make sure to select the "IP addresses" type. Scroll doen to choose a name for your Traget group. Below that, make sure to choose your port number (on the right) from 80 to 8501. Underneath VPC, select the first one. After that scroll all the way down and click on the orange "Next". Once you're on the next page, scroll all the way down and click on the orange "Create target group" button.

## Step 6: Creating the Application Load Balancer
Once you have created the target group, check the left side menu again. Scroll all the way down and select "Load Balancers". It should be above "Target Groups". Click on the orange "Create load balancer" button. Scroll down and select the Application Load Balancer, which is the first option. Click create and it will take you to a new page called "Create Appication Load Balancer. Choose a name for it. After that scroll down to "Network mapping". Click on VPC and select the first one. Underneath "Mappings", select the first two options. Once you have completed that, go to "Security groups" and choose the default one. After that go to "Listeners and routing", and change the port to 8501. On the right of the port is "Default action". Click the dropdown box and select your target group you made earlier. Once you have selected the target group, scroll all the way down and click the orange button that says "Create load balancer".

## Step 7: Running the Task Definition

### SIDE NOTE BEFORE STARTING STEP 7: If you already have an AWS account that has been created for MORE than a year, you will be charged for running EC2 instances. For those UNDERNEATH 12 months of account creation, you will not be charged for using the t2.micro EC2 instance ONLY.

After the load balancer has been created, go back to ECS and click on your cluster name. On the bottom, you have options that say Services, Task Infrastructure, etc. Click on Tasks and click on the orange button "Run new task". You can choose either one. Once you have clicked that you should be in the "Create" menu. Make sure to select "Launch type". Scroll down to "Deployment configuration" and make sure that "Task" is selected. After that, go to "Family" and choose your task definition you made earlier. Once that has been completed, go all the way to the bottom and click on the orange "Create" button. Once this has been done go back to EC2.

## Step 8: Connecting to the Résumé Builder
Once you're in EC2, underneath the "Resources" box, which in the middle of the screen, click on "Instances (running)". Click on the running instance and there should be a box that popped up on the bottom. Copy the Public IPv4 address, which is located to the bottom right side of the screen, and paste it into a new tab DO NOT HIT ENTER. Make sure to add a :8501 at the very end of the link. Once you have done that, hit enter and the page will load up.

### Congratulations! You have sucessfully connected to the Résumé builder! YOU MUST follow Step 9 though!

## Step 9: Stopping the website
Once you are done using the website, make sure to shut it down during idle times to avoid be charged accidentally.

In order to do this, go back to the AWS Management Console and go to ECS. Click on your Cluster and click on the "Tasks" tab again. Click on the "Stop" button to the left of the "Run new task" button. Make sure to choose "stop all tasks" and confirm it. After that go back to EC2. Scroll all the way down on the left hand menu and at the very bottom select "Auto Scaling Groups". Once you are there, click on the group. To the bottom left, there is an "Edit" button. Click on that button. A panel will appear on the screen. Make sure that "Desired Capacity" is set to 0. Do the Same thing for the "Scaling limits" section, make "Min desired capacity" and "Max desired capacity" to 0. DOUBLE CHECK ALL NUMBER ON THE SCREEN ARE 0. After that, click on update. 

After that is done, scroll all the way up to "Instances" and click on it. When you are there, there should be a new search box. To the right of that is a dropdown menu of "Any state" and select "All states". After that there should be an instance there. Make sure that the instance state is "terminated". If it's not, select it and click on "Actions", which is located to the left of the "Launch instances" button. Make sure to click on "Terminate". DO NOT STOP IT, MAKE SURE IT'S terminated. You can double check by checking the EC2 instance and checking the "Instance state". It will say if it is Terminated or not. You can hit the refresh button that is located to the left of the "Instance state button". Once it has been completed terminated, you are done. You can delete everything you created, however it is not necessary.

# That's it! That's how to launch the Résumé Builder through AWS! If you want to re-run the Résumé Builder again and you have all your resources still, you can start at Step 7. For those who have deleted EVERYTHING, you have to start from the beginning.

