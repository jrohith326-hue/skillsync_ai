# core/ai_engine.py

from .models import CareerPath

def recommend_careers(user_skills):
    """
    Returns a list of tuples: (CareerPath, match_score)
    where match_score is between 0 and 100.
    """
    recommendations = []

    for path in CareerPath.objects.all():
        required_skills = path.required_skills.all()
        total_required = required_skills.count()
        matched_skills = [skill for skill in required_skills if skill in user_skills]
        matched_count = len(matched_skills)

        if total_required > 0:
            score = (matched_count / total_required) * 100
            if score >= 40:  # You can change the threshold
                recommendations.append((path, round(score, 2)))

    # Sort by match score descending
    recommendations.sort(key=lambda x: x[1], reverse=True)
    return recommendations
