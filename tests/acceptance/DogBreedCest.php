<?php
use \page\Acceptance\dogbreed;


class DogBreedCest
{
   /* public function _before(AcceptanceTester $I, dogbreed $dogbreed)
    {
        $I->MaximizeWindow();
        $I->amOnPage("/");
        $I->amGoingTo('Login as admin.');
        $I->wait(5);
        $I->click($dogbreed->MenuBtn);  
        $I->wait(1);
        $I->click($dogbreed->loginBtn);  
        $I->wait(2);
        $dogbreed->_setInput($I, $dogbreed->usernameField, 'admin');
        $dogbreed->_setInput($I, $dogbreed->passwordField, 'password');
        $I->click($dogbreed->submitBtn);  
        $I->wait(8);
    }*/

    public function dogbreedidentification(AcceptanceTester $I, dogbreed $dogbreed)
    {
        $I->MaximizeWindow();
        $I->amOnPage("/");
        $I->amGoingTo('Login as admin.');
        $I->wait(5);
        $I->click($dogbreed->MenuBtn);  
        $I->wait(1);
        $I->click($dogbreed->loginBtn);  
        $I->wait(2);
        $dogbreed->_setInput($I, $dogbreed->usernameField, 'admin');
        $dogbreed->_setInput($I, $dogbreed->passwordField, 'password');
        $I->checkOption($dogbreed->submitBtn);
        $I->wait(80);


        $I->amGoingTo('Check the dog breed is correctly identified.');
        $dogbreed->_scrollTo($I, $dogbreed->Predict);
        $I->attachFile($dogbreed->Browsefile, 'dog.jpg');
        $I->wait(5);
        $dogbreed->_scrollTo($I, $dogbreed->Predict);
        $I->click($dogbreed->Predict);  
        $I->wait(10);

        $dogbreed->_scrollTo($I, $dogbreed->Img);
        $I->amGoingTo('Check the dog image is uploaded.');
        $I->seeElement($dogbreed->Img);
        $I->wait(1);

        $dogbreed->_scrollTo($I, $dogbreed->wikipedia);
        $I->amGoingTo('Check the dog breed.');
        $I->see('The Dog Breed is Maltese Dog');
        $I->wait(1);

        $I->amGoingTo('Check the author settings in the frontend.');
        $I->click($dogbreed->wikipedia);  
        $I->wait(2);
    }
}
