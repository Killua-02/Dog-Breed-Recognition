<?php
namespace Page\Acceptance;
use \Facebook\WebDriver\Remote\RemoteWebDriver;
use \Facebook\WebDriver\WebDriverBy;
use \Facebook\WebDriver\WebDriverKeys;

class dogbreed
{
    //before function
    public $MenuBtn = '(//*[@class="st-cc st-d2 st-bq st-d3 st-d4 st-d5"])';
    public $loginBtn = '//*[@id="bui-5"]';
    public $usernameField = '//*[@id="root"]/div[1]/div/div/div/div/section[1]/div[1]/div[2]/div[1]/div/div[2]/div/div[1]/div/input';
    public $passwordField = '//*[@id="root"]/div[1]/div/div/div/div/section[1]/div[1]/div[2]/div[1]/div/div[3]/div/div[1]/div/input';
    public $submitBtn = '//*[@id="root"]/div[1]/div/div/div/div/section[1]/div[1]/div[2]/div[1]/div/div[4]/div/label/span';

    //dog breed identification
    public $Browsefile = '#root > div:nth-child(1) > div > div > div > div > section.main.css-1v3fvcr.egzxvld3 > div > div:nth-child(1) > div > div:nth-child(7) > div > section > input[type=file]';
    public $Predict = '(//*[@class="css-1q8dd3e edgvbvh9"])[2]';
    public $Img = '(//*[@class="css-1v0mbdj etr89bj1"])[2]';
    public $wikipedia = '(//*[@href="https://en.wikipedia.org/wiki/Maltese_Dog"])';

    /**
     * This function scroll to the required selector
     */
    public function _scrollTo($I, $selector)
    {
        $this->field = $selector;
        $field = $I->executeInSelenium(function(RemoteWebDriver $webdriver){
            return $webdriver->findElement(WebDriverBy::xpath($this->field))->getLocationOnScreenOnceScrolledIntoView();
        });
        $I->wait(2);
    }

    /**
     * This function sets given value for given field
     */
    public function _setInput($I, $inputField, $value)
    {
        $I->click($inputField);
        $I->clearField($inputField);
        $I->fillField($inputField, $value);
    }

}
