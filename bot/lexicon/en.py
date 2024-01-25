from typing import Any

LEXICON_EN: dict[str, str] = {
    'language': 'Select your language',
    'welcome': 'Hello! Do you want to find out what could your dream job look like? '
               'My name is Altigus, '
               'and I want to become your personal career guide. How should I call you?',
    'conest_save': 'It is pleasure to serve you, {name}. Now my database contains {count} most popular professions.'
           ' I know, you are special, and it might be pretty time-consuming to select the best '
           'profession especially for you manually, so we will do some AI magic. Let me '
           'first ask you few questions to know you better: it shouldn’t take more than 15 minutes!',
    'no_consest': 'I`m sorry that you didn`t want to take advantage of my opportunities',
    'social': 'When in a social setting, do you prefer to initiate conversations or wait for others to approach you?',
    'group_size': 'Do you feel more comfortable in a large party or in a small group setting?',
    'relax_time': 'After a busy day, do you relax by spending time with friends or by spending time alone?',
    'meeting': 'In meetings, do you prefer to express your opinions freely or reflect on them before speaking?',
    'share': 'Are you more inclined to share personal stories with many people or only with close friends?',
    'focus': 'Do you focus more on the details and specifics of a situation or the overall concept and meaning?',
    'plan': 'When making plans, do you prefer step-by-step guidelines or a general outline?',
    'discussion': 'In discussions, do you base your arguments more on concrete facts or theoretical ideas?',
    'enjoyment': 'Do you find more enjoyment in practical applications or abstract concepts?',
    'learning': 'When learning something new, do you prefer hands-on experience or exploring the underlying theory?',
    'decision': 'Are your decisions more influenced by logical analysis or personal values?',
    'disagreement': 'In a disagreement, do you prioritize being right or maintaining the relationship?',
    'assess_performance': 'Do you assess performance more on objective criteria or individual circumstances?',
    'leadership': 'In a leadership role, do you focus more on task achievement or team morale?',
    'feedback': 'When giving feedback, do you tend to be straightforward and direct or considerate and tactful?',
    'work_time': 'Do you prefer having a structured routine or a flexible schedule?',
    'deadline': 'When faced with a deadline, do you complete tasks well in advance or close to the deadline?',
    'rules': 'Do you prefer to have clear rules and expectations or room for improvisation?',
    'vacation': 'In planning a vacation, do you have an itinerary planned or decide what to do as you go?',
    'satisfaction': 'Do you find satisfaction in reaching a conclusion or in exploring various possibilities?',
    'client_perceiving': 'This is your result:\n',
    'result': 'Your best job alert:\n'
}

BUTTON: dict[str, Any] = {
    'LANGUAGE': {
        'en': 'English',
        'ru': 'Russian',
    },
    'IMPORTANT': {
        '1': 'Important',
        '0': 'No meter'
    },
    'social': ('wait for others to approach you', 'initiate conversations'),
    'group_size': ('small group', 'large party'),
    'relax_time': ('spending time alone', 'spending time with friends'),
    'meeting': ('reflect on opinions before speaking', 'express opinions freely'),
    'share': ('share personal stories with close friends', 'share with many people'),
    'focus': ('focus on details and specifics', 'focus on the overall concept and meaning'),
    'plan': ('prefer step-by-step guidelines', 'prefer a general outline'),
    'discussion': ('base arguments on concrete facts', 'base arguments on theoretical ideas'),
    'enjoyment': ('find enjoyment in practical applications', 'find enjoyment in abstract concepts'),
    'learning': ('prefer hands-on experience', 'prefer exploring the underlying theory'),
    'decision': ('decisions influenced by logical analysis', 'decisions influenced by personal values'),
    'disagreement': ('prioritize maintaining the relationship', 'prioritize being right'),
    'assess_performance': ('assess performance based on objective criteria',
                      'assess performance based on individual circumstances'),
    'leadership': ('focus on team morale', 'focus on task achievement'),
    'feedback': ('tend to be considerate and tactful when giving feedback',
                 'tend to be straightforward and direct when giving feedback'),
    'work_time': ('prefer a structured routine', 'prefer a flexible schedule'),
    'deadline': ('complete tasks well in advance of the deadline', 'complete tasks close to the deadline'),
    'rules': ('prefer clear rules and expectations', 'prefer room for improvisation'),
    'vacation': ('have an itinerary planned', 'decide what to do as you go'),
    'satisfaction': ('find satisfaction in reaching a conclusion',
                     'find satisfaction in exploring various possibilities'),
}

MENU: dict[str, str] = {
    '/start': 'To start working with the Altigus.',
    '/run_quiz': 'start quiz',
    '/language': 'Select your language',
    '/result': 'Get result from ai'
}

