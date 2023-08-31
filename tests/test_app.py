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
    signup = page.locator('p')
    expect(signup).to_have_text('Test sign-up')

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

'''
When we go to List New Space
we should see a page with fields
for the user to enter details of the space
that match the Space object properties
'''

def test_new_space_page_displays(page, test_web_address):
    page.goto(f'http://{test_web_address}/new-space')
    h1_tag = page.locator('h1')
    expect(h1_tag).to_have_text('Enter new space details')

'''
When we click the field with the appropriate attribute
we can add that detail to the form
'''
def test_add_new_space_with_attribute_details(page, test_web_address, db_connection):
    db_connection.seed('seeds/makersbnb.sql')
    page.goto(f'http://{test_web_address}/new-space')
    page.fill('text=Space Name', 'Test new space')
    # page.fill('text=Description', 'Test description')
    # page.fill('text=Start date', '2023-03-01')
    # page.fill('text=End date', '2023-03-15')
    # page.fill('text=Price per night', 2000)

    page.click('text=Add new space')
    name_element = page.locator('.t-name')
    expect(name_element).to_have_text('Test new space')
    
    