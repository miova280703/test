package com.example;

import static org.junit.Assert.assertTrue;

import org.junit.Test;
import org.junit.Before;
import org.junit.After;
import static org.junit.Assert.*;
import static org.hamcrest.CoreMatchers.is;
import static org.hamcrest.core.IsNot.not;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.firefox.FirefoxDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.remote.RemoteWebDriver;
import org.openqa.selenium.remote.DesiredCapabilities;
import org.openqa.selenium.Dimension;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.interactions.Actions;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.Alert;
import org.openqa.selenium.Keys;
import org.openqa.selenium.JavascriptExecutor;

import java.util.*;
import java.net.MalformedURLException;
import java.net.URL;
import java.lang.Thread;

public class FlujoCompleto {
    private WebDriver driver;
    private Map<String, Object> vars;
    JavascriptExecutor js;

    @Before
    public void setUp() {
        driver = new ChromeDriver();
        js = (JavascriptExecutor) driver;
        vars = new HashMap<String, Object>();
    }

    @After
    public void tearDown() {
        driver.quit();
    }

    public String waitForWindow(int timeout) {
        try {
            Thread.sleep(timeout);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        Set<String> whNow = driver.getWindowHandles();
        Set<String> whThen = (Set<String>) vars.get("window_handles");
        if (whNow.size() > whThen.size()) {
            whNow.removeAll(whThen);
        }
        return whNow.iterator().next();
    }

    /**
     * Flujo Completo, las 5 pruebas juntas
     * 
     * @throws InterruptedException
     */
    @Test
    public void Flujo() throws InterruptedException {
        /* INICIO PRUEBA 1 */
        driver.get("https://demoqa.com/");
        driver.manage().window().setSize(new Dimension(1920, 1053));
        driver.findElement(By.cssSelector(".card:nth-child(1) svg")).click();
        Thread.sleep(1000);
        driver.findElement(By.cssSelector(".show #item-1 > .text")).click();
        Thread.sleep(1000);
        driver.findElement(By.cssSelector(".rct-icon-expand-all")).click();
        Thread.sleep(1000);
        driver.findElement(By.cssSelector(".rct-node:nth-child(3) .rct-node:nth-child(2) .rct-checkbox > .rct-icon"))
                .click();
        Thread.sleep(1000);
        driver.findElement(By.cssSelector(".rct-node:nth-child(3) .rct-node:nth-child(1) .rct-checkbox > .rct-icon"))
                .click();
        Thread.sleep(1000);

        /* INICIO PRUEBA 2 */
        driver.findElement(By.xpath("//div/div[2]/div/div")).click();
        Thread.sleep(1000);
        WebElement elements = driver.findElement(By.xpath("//li[9]/span"));
        ((JavascriptExecutor) driver).executeScript("arguments[0].scrollIntoView(true);", elements);
        elements.click();
        Thread.sleep(1000);
        driver.findElement(By.xpath("//div[2]/div[2]/div[2]")).click();
        Thread.sleep(6000);
        driver.findElement(By.id("enableAfter")).click();
        Thread.sleep(1000);

        /* INICIO PRUEBA 3 */
        driver.findElement(By.id("item-3")).click();
        Thread.sleep(1000);
        driver.findElement(By.cssSelector("#delete-record-1 path")).click();
        Thread.sleep(1000);
        driver.findElement(By.id("addNewRecordButton")).click();
        Thread.sleep(1000);
        driver.findElement(By.id("firstName")).click();
        Thread.sleep(500);
        driver.findElement(By.id("firstName")).sendKeys("Juan");
        Thread.sleep(500);
        driver.findElement(By.id("lastName")).click();
        Thread.sleep(500);
        driver.findElement(By.id("lastName")).sendKeys("Perez");
        Thread.sleep(500);
        driver.findElement(By.id("userEmail")).click();
        Thread.sleep(500);
        driver.findElement(By.id("userEmail")).sendKeys("test@test.bi.com.gt");
        Thread.sleep(500);
        driver.findElement(By.id("age")).click();
        Thread.sleep(500);
        driver.findElement(By.id("age")).sendKeys("24");
        Thread.sleep(500);
        driver.findElement(By.id("salary")).click();
        Thread.sleep(500);
        driver.findElement(By.id("salary")).sendKeys("8000");
        Thread.sleep(500);
        driver.findElement(By.id("department")).click();
        Thread.sleep(500);
        driver.findElement(By.id("department")).sendKeys("Guatemala");
        Thread.sleep(500);
        driver.findElement(By.id("submit")).click();
        Thread.sleep(1000);

        // /* INICIO PRUEBA 4 */
        driver.findElement(By.cssSelector(".element-group:nth-child(1) .header-wrapper")).click();
        Thread.sleep(1000);
        driver.findElement(By.cssSelector(".element-group:nth-child(2) .header-wrapper")).click();
        Thread.sleep(1000);
        driver.findElement(By.cssSelector(".show #item-0")).click();
        Thread.sleep(1000);

        Thread.sleep(500);
        driver.findElement(By.id("firstName")).click();
        Thread.sleep(300);
        driver.findElement(By.id("firstName")).sendKeys("Iovana");
        Thread.sleep(300);
        driver.findElement(By.id("lastName")).click();
        Thread.sleep(300);
        driver.findElement(By.id("lastName")).sendKeys("Miranda");
        Thread.sleep(300);
        driver.findElement(By.id("userEmail")).click();
        Thread.sleep(300);
        driver.findElement(By.id("userEmail")).sendKeys("test@test.bi.com.gt");
        Thread.sleep(300);
        driver.findElement(By.cssSelector(".custom-radio:nth-child(2) > .custom-control-label")).click();
        Thread.sleep(500);
        driver.findElement(By.id("userNumber")).click();
        Thread.sleep(500);
        driver.findElement(By.id("userNumber")).sendKeys("1234567890");
        Thread.sleep(500);
        driver.findElement(By.id("dateOfBirthInput")).click();
        {
            WebElement dropdown = driver.findElement(By.cssSelector(".react-datepicker__month-select"));
            dropdown.findElement(By.xpath("//option[. = 'July']")).click();
        }
        {
            WebElement element = driver.findElement(By.cssSelector(".react-datepicker__month-select"));
            Actions builder = new Actions(driver);
            builder.moveToElement(element).clickAndHold().perform();
        }
        {
            WebElement element = driver.findElement(By.cssSelector(".react-datepicker__month-select"));
            Actions builder = new Actions(driver);
            builder.moveToElement(element).perform();
        }
        {
            WebElement element = driver.findElement(By.cssSelector(".react-datepicker__month-select"));
            Actions builder = new Actions(driver);
            builder.moveToElement(element).release().perform();
        }
        {
            WebElement dropdown = driver.findElement(By.cssSelector(".react-datepicker__year-select"));
            dropdown.findElement(By.xpath("//option[. = '1998']")).click();
        }
        {
            WebElement element = driver.findElement(By.cssSelector(".react-datepicker__year-select"));
            Actions builder = new Actions(driver);
            builder.moveToElement(element).clickAndHold().perform();
        }
        {
            WebElement element = driver.findElement(By.cssSelector(".react-datepicker__year-select"));
            Actions builder = new Actions(driver);
            builder.moveToElement(element).perform();
        }
        {
            WebElement element = driver.findElement(By.cssSelector(".react-datepicker__year-select"));
            Actions builder = new Actions(driver);
            builder.moveToElement(element).release().perform();
        }
        Thread.sleep(500);
        driver.findElement(By.cssSelector(".react-datepicker__day--028:nth-child(3)")).click();
        Thread.sleep(500);
        driver.findElement(By.cssSelector(".subjects-auto-complete__value-container")).click();
        // Thread.sleep(1000);
        WebDriverWait wait = new WebDriverWait(driver, 10);
        WebElement element = wait
                .until(ExpectedConditions.visibilityOfElementLocated(By.id("react-select-2-option-0")));
        // element.sendKeys("Maths");
        element.click();
        Thread.sleep(500);
        driver.findElement(By.cssSelector(".custom-checkbox:nth-child(3) > .custom-control-label")).click();
        Thread.sleep(500);
        WebElement fileInput = driver.findElement(By.id("uploadPicture"));
        String filePath = "/home/iova/prueba.txt";
        fileInput.sendKeys(filePath);
        Thread.sleep(500);
        driver.findElement(By.id("currentAddress")).click();
        Thread.sleep(500);
        driver.findElement(By.id("currentAddress"))
                .sendKeys("Banco Industrial Zona 4. 7a. Avenida 5-10, Zona 4 Centro Financiero Torre I");
        Thread.sleep(300);
        // driver.findElement(By.cssSelector(".css-1gtu0rj-indicatorContainer >
        // .css-19bqh2r")).click();
        WebDriverWait wait1 = new WebDriverWait(driver, 10); // Esperar un máximo de 10 segundos
        WebElement element1 = wait1
                .until(ExpectedConditions
                        .presenceOfElementLocated(By.cssSelector(".css-1gtu0rj-indicatorContainer >.css-19bqh2r")));
        element1.click();
        WebDriverWait wait2 = new WebDriverWait(driver, 10); // Esperar un máximo de 10 segundos
        WebElement element2 = wait2
                .until(ExpectedConditions.presenceOfElementLocated(By.id("react-select-3-option-0")));
        element2.click();
        Thread.sleep(300);
        WebDriverWait wait3 = new WebDriverWait(driver, 10); // Esperar un máximo de 10 segundos
        WebElement element3 = wait3
                .until(ExpectedConditions
                        .presenceOfElementLocated(By.cssSelector(".css-1gtu0rj-indicatorContainer >.css-19bqh2r")));
        element3.click();
        WebDriverWait wait4 = new WebDriverWait(driver, 10); // Esperar un máximo de 10 segundos
        WebElement element4 = wait4
                .until(ExpectedConditions.presenceOfElementLocated(By.id("react-select-4-option-0")));
        element4.click();
        Thread.sleep(5000);

        WebDriverWait wait5 = new WebDriverWait(driver, 10);
        WebElement button = wait5.until(ExpectedConditions.elementToBeClickable(By.id("submit")));
        button.click();
        Thread.sleep(1000);
        driver.findElement(By.id("closeLargeModal")).click();

        /* INICIO PRUEBA 5 */
        driver.findElement(By.cssSelector(".element-group:nth-child(2) .header-wrapper")).click();
        Thread.sleep(1000);
        driver.findElement(By.cssSelector(".element-group:nth-child(6) .header-text")).click();
        Thread.sleep(1000);

        WebElement elemen = driver.findElement(By.cssSelector(".show #item-2 > .text"));
        ((JavascriptExecutor) driver).executeScript("arguments[0].scrollIntoView(true);", elemen);
        elemen.click();
        Thread.sleep(1000);
        js.executeScript("window.scrollTo(0,0)");
        Thread.sleep(1000);
        driver.findElement(By.id("searchBox")).click();
        driver.findElement(By.id("searchBox")).sendKeys("Understanding ECMAScript 6");
        driver.findElement(By.linkText("Understanding ECMAScript 6")).click();
        Thread.sleep(1000);
        vars.put("window_handles", driver.getWindowHandles());
        Thread.sleep(1000);
        driver.findElement(By.cssSelector("#website-wrapper #userName-value")).click();
        vars.put("win203", waitForWindow(4000));
        vars.put("root", driver.getWindowHandle());
        Thread.sleep(1000);
        driver.switchTo().window(vars.get("win203").toString());
        Thread.sleep(1000);
        driver.close();
        Thread.sleep(1000);
        driver.switchTo().window(vars.get("root").toString());
        driver.findElement(By.id("addNewRecordButton")).click();
        Thread.sleep(1000);
    }
}
