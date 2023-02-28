To get started with Solid Pod development a Solid Pod and a webID are needed. Furthermore, an APP with a user interface has been developed as part of the Solid Pod PoC. This enables users to easily access and edit the data stored on their Solid Pod as well as manage the folders and privacy settings of the documents on an individual basis. In this section, we walk the reader through the steps necessary for running the Application.

Building a SolidPod App:
The application uses Inrupt’s JavaScript Client Libraries to read and write to the user profile. There are also other libraries that can be used as well as other programming languages that support Solid. However, Inrupt’s library is to this day the most fully-developped library for the Solid project. Moreover, tutorial uses npm and Parcel to run the application locally on localhost:1234.

To run the API, a few steps need to be executed:

1. Clone the Repository and change to the relevant branch: Run the command the
following command in a WSL2 terminal.

    • git clone https://github.com/Cyr-Ch/Convolut.git

    • cd Convolut

    • git checkout cyrch/solidpods
  
2. Install nvm, node.js, and npm: Follow the instructions here.

3. Install the Inrupt Client Libraries: Run the following command in the same WSL2 terminal.

    • npm install @inrupt/solid-client @inrupt/solid-client-authn-browser @inrupt/vocab-common-rdf
  
4. Install Parcel: Run the following command in the same WSL2 terminal.

    • npm install parcel-bundler
  
5. Launch the Application: Run the command in the same WSL2 terminal

    • npx parcel index.html
  
6. Open localhost:1234 in a browser
