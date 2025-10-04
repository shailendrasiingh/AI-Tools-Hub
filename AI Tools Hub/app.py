from flask import Flask, render_template, request, url_for
import json

app = Flask(__name__)

# Load tools data from JSON file
def load_tools():
    try:
        with open('tools.json', 'r') as file:
            data = json.load(file)
        return data['tools']
    except FileNotFoundError:
        return []

# Categorize tools by page field
def categorize_tools(tools):
    categorized = {
        'learning': [],
        'resources': [],
        'career': []
    }
    
    for tool in tools:
        page = tool.get('page', '').lower()
        if page in categorized:
            categorized[page].append(tool)
    
    return categorized

@app.route('/')
def index():
    tools = load_tools()
    categorized_tools = categorize_tools(tools)
    return render_template('index.html', categorized_tools=categorized_tools)

@app.route('/category/<category_name>')
def category(category_name):
    tools = load_tools()
    categorized_tools = categorize_tools(tools)
    
    # Get search query from URL parameters
    search_query = request.args.get('q', '')
    selected_hashtag = request.args.get('hashtag', '')
    
    # Filter tools based on category
    category_tools = categorized_tools.get(category_name, [])
    
    # Apply search filter if provided
    if search_query:
        category_tools = [tool for tool in category_tools 
                         if search_query.lower() in tool['name'].lower() 
                         or search_query.lower() in tool['description'].lower()
                         or search_query.lower() in tool['category'].lower()]
    
    # Apply hashtag filter if provided
    if selected_hashtag:
        category_tools = [tool for tool in category_tools 
                         if selected_hashtag in tool['hashtags']]
    
    # Get all unique hashtags from the category tools
    all_hashtags = set()
    for tool in categorized_tools.get(category_name, []):
        for tag in tool['hashtags']:
            all_hashtags.add(tag)
    
    # Define category titles and descriptions
    category_info = {
        'learning': {
            'title': 'AI Tools for Learning Support',
            'description': 'Discover powerful AI tools to enhance your learning experience'
        },
        'resources': {
            'title': 'Study Resources & Content Hub',
            'description': 'Find valuable resources to support your studies'
        },
        'career': {
            'title': 'Career & Skill Development',
            'description': 'Tools and resources to advance your career'
        }
    }
    
    current_category = category_info.get(category_name, {'title': 'Category', 'description': ''})
    
    return render_template('category.html', 
                         tools=category_tools,
                         category_name=category_name,
                         category_title=current_category['title'],
                         category_description=current_category['description'],
                         search_query=search_query,
                         selected_hashtag=selected_hashtag,
                         all_hashtags=sorted(all_hashtags))

# Additional pages
@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/faq')
def faq():
    return render_template('faq.html')

@app.route('/privacy')
def privacy():
    return render_template('privacy.html')

@app.route('/terms')
def terms():
    return render_template('terms.html')

if __name__ == '__main__':
    app.run(debug=True)