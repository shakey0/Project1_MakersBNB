from playwright.sync_api import Page, expect

# Tests for your routes go here

# """
# We can render the index page
# """
# def test_get_index(page, test_web_address):
#     # We load a virtual browser and navigate to the /index page
#     page.goto(f"http://{test_web_address}/index")

#     # We look at the <p> tag
#     strong_tag = page.locator("p")

#     # We assert that it has the text "This is the homepage."
#     expect(strong_tag).to_have_text("This is the homepage.")

'''
When we visit the home page,
we should see a welcome message
'''
def test_welcome_message_displays(page, test_web_address):
    page.goto(f'http://{test_web_address}/')
    h1_tag = page.locator('h1')
    expect(h1_tag).to_have_text("Welcome to MakersBnB!")

def test_welcome_buttons(page, test_web_address):
    page.goto(f'http://{test_web_address}/')
    buttons = page.locator('.t-buttons')
    expect(buttons).to_have_text('Login\nSign-up')

def test_click_signup_button(page, test_web_address):
    page.goto(f'http://{test_web_address}/')
    page.click("text='Sign-up'")
    header = page.locator('.t-header')
    expect(header).to_have_text('Sign up to MakersBNB')
    email = page.locator('.t-email')
    expect(email).to_have_text('Email address:')
    password = page.locator('.t-password')
    expect(password).to_have_text('Password:')
    confirm_password = page.locator('.t-confirm_password')
    expect(confirm_password).to_have_text('Confirm password:')


def test_click_homepage_login_button(page, test_web_address):
    page.goto(f'http://{test_web_address}/')
    page.click("text='Login'")
    header = page.locator('.t-header')
    expect(header).to_have_text('Please Login')
    email = page.locator('.t-email')
    expect(email).to_have_text('Email address:')
    password = page.locator('.t-password')
    expect(password).to_have_text('Password:')

def test_login_page_available_spaces_get_route(page, test_web_address):
    page.goto(f'http://{test_web_address}/')
    page.click("text='Login'")
    page.click("text='Login'")
    p_tag = page.locator('p')
    expect(p_tag).to_have_text('Test Available Spaces')

def test_sign_up_page_enter_invalid_email_address(page, test_web_address):
    page.goto(f'http://{test_web_address}/')
    page.click("text='Sign-up'")
    page.fill("input[name=email]", "ksfuhoief")
    page.click("text='Sign-up'")
    error = page.locator('.error')
    expect(error).to_have_text('ksfuhoief is not a valid email address')

def test_sign_up_page_enter_invalid_password(page, test_web_address):
    page.goto(f'http://{test_web_address}/')
    page.click("text='Sign-up'")
    page.fill("input[name=email]", "makers@makers.d")
    page.fill("input[name=password]", "lkfek")
    page.click("text='Sign-up'")
    errors = page.locator('.error')
    expect(errors).to_have_text(['Password must be at least 8 characters.', 
                                'Password must contain uppercase and lowercase characters.',
                                'Password must contain at least 1 number.', 
                                'Password must contain at least 1 symbol.' 
])

def test_sign_up_page_enter_non_identical_passwords(page, test_web_address):
    page.goto(f'http://{test_web_address}/')
    page.click("text='Sign-up'")
    page.fill("input[name=email]", "makers@makers.d")
    page.fill("input[name=password]", "Makersbnbpassword!23")
    page.fill("input[name=confirm_password]", "aaaa")
    page.click("text='Sign-up'")
    error = page.locator('.error')
    expect(error).to_have_text('passwords do not match')

def test_sign_up_page_goes_through_to_available_spaces_page(page, test_web_address):
    page.goto(f'http://{test_web_address}/')
    page.click("text='Sign-up'")
    page.fill("input[name=email]", "makers@makers.d")
    page.fill("input[name=password]", "Makersbnbpassword!23")
    page.fill("input[name=confirm_password]", "Makersbnbpassword!23")
    page.click("text='Sign-up'")
    text = page.locator('p')
    expect(text).to_have_text('Test Available Spaces')


