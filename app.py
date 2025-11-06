from flask import Flask, request, render_template_string

app = Flask(__name__)

HTML_PAGE = """
<!doctype html>
<html>
<head>
    <title>Software Effort Estimator</title>
</head>
<body style="font-family: Arial; margin: 40px;">
    <h2>Software Effort Estimation (COCOMO Model)</h2>
    <form method="post">
        <label>Enter Lines of Code (LOC):</label><br>
        <input type="number" name="loc" required><br><br>

        <label>Select Project Type:</label><br>
        <select name="complexity">
            <option value="organic">Organic</option>
            <option value="semi-detached">Semi-Detached</option>
            <option value="embedded">Embedded</option>
        </select><br><br>

        <input type="submit" value="Estimate">
    </form>

    {% if effort %}
        <hr>
        <h3>Results:</h3>
        <p><b>Effort:</b> {{ effort }} Person-Months</p>
        <p><b>Estimated Cost:</b> ₹{{ cost }}</p>
    {% endif %}
</body>
</html>
"""

def cocomo_estimate(loc, complexity):
    kloc = loc / 1000  # convert LOC to KLOC

    if complexity == "organic":
        a, b = 2.4, 1.05
    elif complexity == "semi-detached":
        a, b = 3.0, 1.12
    elif complexity == "embedded":
        a, b = 3.6, 1.20
    else:
        a, b = 2.4, 1.05  # default

    effort = a * (kloc ** b)  # person-months
    cost = round(effort * 50000, 2)  # assuming ₹50,000 per month
    return round(effort, 2), cost


@app.route("/", methods=["GET", "POST"])
def index():
    effort = cost = None
    if request.method == "POST":
        loc = float(request.form["loc"])
        complexity = request.form["complexity"]
        effort, cost = cocomo_estimate(loc, complexity)
    return render_template_string(HTML_PAGE, effort=effort, cost=cost)


if __name__ == "__main__":
    app.run(debug=True)
