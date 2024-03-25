# README
# Here are the instructions for creating a Pipeline in Azure

## Step 1: Logging into Microsoft Azure Portal
Visit the [Azure Portal](https://login.microsoftonline.com/organizations/oauth2/v2.0/authorize?client_id=8e0e8db5-b713-4e91-98e6-470fed0aa4c2&response_type=code%20id_token&scope=openid%20profile&state=OpenIdConnect.AuthenticationProperties%3DX6HflknqpQ9Rz9BE6WDdPf63zubJhSMbgpQbwMzab6ZGFzkPVsenUtfBphvPpQb79pUTz70aQuRERpTvhJ-qNi96m0HAk14EatmGLLThIq9lj9QHYnuzrVJnRlkK3rVrfb_j4Yo9IkoIUmMHyvecCTpDwV0ZjZx6ZWDezeItq68mCEYvU8_dYmkFYzWxRJXfffPoLGsqk1cwdk8si-_pIEMbG04fQGnwD11S_bsZ0exf2M0hu2lvODBU68bFFmxESGLnF4k30afYhTezNOWAo7NFrB1ka7dZ1di8RVL4rM8xWdNXIW6gZVgAqLdMc3Kyh5AMidWfUC_ikjFV_8l3v4jMCaKqNwtgkA3uzh7CiZDNEo7CR3Hw_aK_MQMlJYg4D3bVHdjU_VbKmyayq93NjgvGNV5FrLMLMBF3YkrLsqQ-Lw2PrPxJiCkOoS5VVjHfKJvO6tGFwcMgHABdZESziRToH-6L-cE8PnIWaa1KbyI&response_mode=form_post&nonce=638453466168436112.MjY2OWM4N2QtY2YxZS00ZWQ5LWEyYWMtOTRjZDRlMWI3NGE2N2FhODMyYTItNzNkNS00ZTg3LWFmYTYtZGViZDNhZWViZThl&redirect_uri=https%3A%2F%2Fsignup.azure.com%2Fapi%2Fuser%2Flogin&max_age=86400&post_logout_redirect_uri=https%3A%2F%2Fsignup.azure.com%2Fsignup%3Foffer%3Dms-azr-0044p%26appId%3D102%26ref%3D%26redirectURL%3Dhttps%3A%2F%2Fazure.microsoft.com%2Fget-started%2Fwelcome-to-azure%2F%26l%3Den-us%26srcurl%3Dhttps%3A%2F%2Fazure.microsoft.com%2Ffree&x-client-SKU=ID_NET472&x-client-ver=6.34.0.0) login site. Once you're there, you can login with your Microsoft Account or GitHub Account. If you don't have an account, [create one](https://signup.live.com/signup?sru=https%3a%2f%2flogin.live.com%2foauth20_authorize.srf%3flc%3d1033%26client_id%3d51483342-085c-4d86-bf88-cf50c7252078%26cobrandid%3d788a943c-8e34-4c0a-9c83-1e4ef0322879%26mkt%3dEN-US%26opid%3d3EA7709F52B70C19%26opidt%3d1709749831%26uaid%3d7bef474f156b4cd78c07e0f554279ac6%26contextid%3d2BAF8C255A9D4A1B%26opignore%3d1&mkt=EN-US&uiflavor=web&lw=1&fl=easi2&cobrandid=788a943c-8e34-4c0a-9c83-1e4ef0322879&client_id=51483342-085c-4d86-bf88-cf50c7252078&uaid=7bef474f156b4cd78c07e0f554279ac6&suc=8e0e8db5-b713-4e91-98e6-470fed0aa4c2&lic=1).

## Step 2: Creating a Resource Group
Once you are in the Azure Portal, go to the top and click on the search bar and type in resource groups. Click on the first option. Once you're in the Resource groups page, click on the Create button to the left. Make sure to select your Azure Subscription and name your Resource group. After that click on the white Review + create button on the bottom left.

## Step 3: Creating a Container Registry
Click back on the search bar and type in container registry. Click on the first option. Now that we're in the page, click on the Create button, which is on the left side of the screen. Once again, choose the subscription and resource group. After that, choose a Registry name. Once you have chosen your name, go to the bottom where it says "Pricing plan". Make sure to select Basic. After that, click on the blue Review + create button on the bottom left.

Once it's created, click on it and you should be in a new screen. Underneath Essentials on the middle of the page, copy the subscription ID and save it somewhere. Do the same with the login server name which is located to the right of the screen. This will be important for later.

## Step 4: Logging into Azure DevOps
Visit the [Azure DevOps](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwj02qWXn-CEAxVZ4ckDHf4cA4gQFnoECBEQAQ&url=https%3A%2F%2Faex.dev.azure.com%2F&usg=AOvVaw2AXOivxL9pU4DLElYv2Tjc&opi=89978449) login site. Once you're there, you can login with your Microsoft Account or GitHub Account that you used for the Azure Portal. After that, click on "Create new organization". It will lead you to a new tab. On there, you can rename your organization if you choose to. After that make sure that the projects are hosted in the United States. After that, enter in the characters and click on the blue "Continue" button.

## Step 5: Create a Project
Once you're on the website, first copy your link on the top, you will need it for later. After that, enter in a name for the project. After that, choose a project name and choose the public visibility. Click on the blue "Create project" button. 

If you public is not avaiable click on the link below that that has "organization policies" underlined in blue. Go click on the Allow public projects and make sure its on. A prompt will pop up and choose the save button. Click on the Azure DevOps on the top left of the screen. Recreate the project from the information above.

## Step 6: Import the GitHub Repository
Now that the project has been created, look on the left hand side and choose Repos, which has an orange symbol next to it. When you're in Repos, there will be a section called "Import a repository". Click the import button. Input this Clone Url: https://github.com/sliem77/resume-builder . Click on import. The Repository Information is now inside of your Project.

## Step 7: Creating an Agent Pool
This part is extremely important and vital for the project to even work, so please do not skip this step. 

Before starting, make sure your click on the person gear icon to the left your your profile pic in the top right. Click on it. Click on the option "Personal access tokens". Click the blue button that says "New token". Choose any name for it. In the scopes tab, select Full access. Click on the blue "Create" button on the bottom. You will be led to a new prompt, make sure to copy and paste that somewhere, you will need it.

On the bottom of the screen, you should see project settings, which has a gear to the left of it. Click on that. It will now lead you to a new page. Scroll down to see the pipelines section and click on the first option called "Agent Pool". Once you're in the agent pool section click on the blue "Add pool" button to the right of the screen. A new tab will pop up that says "Agent Pool." Click on the "Pool type" drop-down box. Click on the "Self hosted" option and name it "new-agent-pool". After that, make sure to check the box that says grant access permission to all pipelines. After this, click on the "Create" button on the bottom of the screen. After this, go back into Agent pools and click on the new agent pool that was just created. To the right, there should be a "New agent" button. Click on that. A prompt will pop up. Click on the "Download" button. Open up your Terminal (Mac) or Command Prompt (Windows). cd into your Downloads folder. After that, follow the instructions that are below the Download button.

For Windows users, copy and paste everything after the ">" symbol.

For Mac and Linux Users, copy and pasted everything after "$" symbol.

When running ./config.sh or ./config.cmd, Terminal/Command Prompt will ask for the server url. Paste in the link mentioned in Step 5. After that, for "Authentication type" hit enter. "Personal access token" will appear, paste in the code that you copied earlier. Hit enter. "New agent pool" shows up, make sure to type in "new-agent-pool". Hit enter. A new line will appear, hit enter once again. After that, a "_work" folder will appear, hit enter. The next line asks for yes or no, type in Y. Hit enter. Hit enter again for the next line.

If you get any error, just ignore it and run the script, either .\run.cmd for Windows or .\run.sh for Mac.

Make sure that Terminal/Command Prompt is open. You may close it after you are done with the resume builder

## Step 7.1: IMPORTANT FOR MAC USERS ONLY

You will most likely run into the issue of "“Agent.Listener” can’t be opened because Apple cannot check it for malicious software." To solve this, type in the following commands:

sudo spctl --master-disable

echo Disabled Protections
### MAKE SURE TO RUN THIS SCRIPT AFTER YOU ARE DONE WITH RUNNING THE PROGRAM IN TERMINAL:
sudo spctl --master-enable

echo Enabled Protections
### DO NOT FORGET THIS STEP!

## Step 8: Creating a Service Connection
Go back to project settings and select "Service Connections", which is below the agent pools section. Once your there, click on Create service connection. Select Docker registry and click on the "Next" button. For Registry type, choose Azure Container Registry. Choose Service Principal for Authentication Type. A new page will pop up asking for your login. Put in your credentials and login. After that, select your container registry in the Azure container registry dropdown box. Now choose a name for your Service Connection. You can add a description if you choose to. After that, make sure that the checkbox below is checked. Click on "Save"

## Step 9: Logging into Docker
Before starting, open up Docker and make sure it's open.

Now that the service connection has been done, go back to your container registry. Once you're there, go to access keys, which is located to the left of the screen. It has a key symbol to the left of it. Once you're there, make sure to copy the Login server. After that check the "Admin user" box. After that, there will be a Username and 2 passwords underneath it. Open up Terminal/Command Prompt and type in the following:

docker login <login_server>

The login_server is your login server that you copied earlier. After running that command, copy and paste one of the passwords that were given to you which are underneath the username box. The password WILL show up as blank on Terminal/Command Prompt. Once that's done, you will get a login succeeded.

## Step 10: Creating the Pipeline
After that, click on your project and look on the left hand side of the screen and choose Pipelines. Pipelines has a blue spaceship symbol. When you're in Pipelines, click on the blue "Create Pipeline" button. Choose the first option "Azure Repos Git". You will be led to a "Select a repository", make sure to click the first option. When you are in the "Configure" stage, choose the option "Existing Azure Pipelines YAML file". Once you're there, choose the path that says azure-pipelines.yml. When you get to the code, replace the "dockerRegistryServiceConnection" on line 12 with the subscription ID you copied from step 3. Along with that, copy and paste the login server from before and replace the value on line 14. After that, click on the "Variables" button which is to the left of the blue "Run" button. Click on "New variable". For the name, type in "OPENAI_API_KEY". For the value, type in your OpenAI API Key and MAKE SURE THAT YOU CHECKED THE BOX "Keep this value secret". THIS IS VERY IMPORTANT, SO MAKE SURE ITS DONE. If you don't have one, please refer to the "README - Using the Résumé Builder.md" file. After this, click on the "OK" button on the bottom right. If a resource authorization appears, click on the Resource Authorized button to the right of it. After that, hit the "Run" button. You will be led to a new page where everything is running. If you aren't led anywhere, underneath Jobs, click on the "build" that has a blue symbol on the left of it. Wait for the everything under "Build stage" to have a check on the left side to it.

## Step 11: Hosting the Azure Website
Go back to the Azure Portal and click on the "Search" Button to the top of the screen. Type in App Services and click on the first one. Now you are on the App Services page, click on the "+ Create" button to the left of the screen underneath the "App Services" title. Click on the first option that says "+ Web App". Make sure for resource group click on the blue "Create new" button. Choose a name for the resource group and click on "OK" right underneath it. After that, choose a name for your web app. Underneath that, make sure to click on "Docker container". Scroll down and make sure to select Free F1 for pricing plan. After that, scroll up to the top of the screen and click on the Docker tab right next to database on the top of the screen right below the "Create Web App" title. Click on the image source drop-down box and make sure to choose "Azure Container Registry". Below that, select the registry, image, and tag boxes below the "Azure container registry options". Click on the blue "Review + create" button on the bottom of the screen. After that so once again for "App services", Wait for a few minutes and then hit the refresh button right next to manage view. After that, your website should pop up. Click on it, and copy your website, which is shown underneath default domain. Your web services should look like this: *APPNAME*.azurewebsites.net. Paste it into a new tab and wait for a few minutes for the résumé builder to launch. Once it has been launched, you're good to go!

# That's it! That's all you need for launching the résumé builder in Azure!