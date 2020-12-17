# Let's create an architecture for an IT company
# We have sale persons. They have a first_name, last_name, number_of_sales, sales_talent (from 1 to 10)
# We have product owners. They have a first_name, last_name, managed teams, managing_talent (from 1 to 10)
# We have devs. They have a first_name, last_name, years_of_experience, backend_skill(1-10), frontend_skill(1-10),
#                           devops_skill(1-10), system_knowledge(1-10), testing_skill(1-10), designer_skill(1-10),
#                           teams
# Junior devs 0-2 years of experience, 3-5 mid level, 6+ senior level
# A junior backend dev has backend_skill > 5, mid > 7, senior > 9. The same for the rest of the skills.
# Frontend dev => frontend_skill, Devops => devops_skill, SystemEngineer => system_knowledge, QA => testing skill,
# UX => designer_skill, FullStack (only seniors) => frontend + backend + system
# A dev can have multiple roles if he has enough skill, examples: backend + devops, UX + frontend
# Teams of devs: team_name, project_name, design (0 or 1 UX dev), qa (1 QA dev), devops(1 Devops),
#                frontend (1 Senior frontend & 1 junior frontend), system (0/1 SystemEngineer)
#                backend (1 Senior backend + 1 mid or 2 juniors), product_owner
# UX, QA, Devops & SystemEngineers can be in multiple teams
# We have share holders. They have a first_name, last_name, percentage_of_shares. They have a job in the company, too.
# They can be sale person, product owner or a dev.

# Create a company with 3 sale persons, 4 share holders, 2 product_owners, 4 dev teams
# Devs: 1 Senior UX & 1 Mid UX, 1 Senior QA, 1 Mid QA, 1 Junior QA, 1 Senior devops, 1 junior devops, 3 Senior frontend,
#         2 Mid frontend, 3 junior frontend, 1 System Engineer, 4 Senior backend, 3 Mid backend, 5 junior backend
