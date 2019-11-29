# from django.template import loader
from random import *

from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from authentification.models import Profile
from .models import Exam, Free_Text, Question, One_answer, Multichoice, Answer, Groupst


def home(request):
    return render(request, 'exam/index.html')


def message(request):
    return render(request, 'exam/message.html')


# créer les examens
def create_exam(request):
    if request.method == 'POST':
        examName = request.POST['examName']
        ExamDesc = request.POST['ExamDesc']
        category = request.POST['category']
        logo = request.FILES['logo']
        mode1 = request.POST['mode']
        score = request.POST['success_score']
        timer1 = request.POST['timer']

        exam = Exam()
        exam.name = examName
        exam.description = ExamDesc
        exam.category = category
        exam.logo = logo
        exam.mode = mode1
        exam.success_score = score
        exam.timer = timer1
        exam.prof = request.user

        exam.save()
        return render(request, 'exam/create_exam.html')
    else:
        return render(request, 'exam/create_exam.html')


# afficher la liste des examens
def active_exams(request):
    exams = Exam.objects.filter(prof=request.user)
    exams = Exam.objects.filter(prof=request.user)
    context = {'exams': exams}
    return render(request, 'exam/active_exams.html', context)


# créer les différents types des questions

def create_question(request, pk):
    if request.method == 'POST':
        qdes = request.POST['qdes']
        qpoint = request.POST['qpoint']
        qht = request.POST['qht']
        qft = request.POST['qft']
        success_msg = request.POST['success_msg']
        fail_msg = request.POST['fail_msg']
        type = request.POST['type']
        correct = request.POST['correct_answer']

        question = Question()

        question.ex = Exam.objects.get(pk=pk)
        question.description = qdes
        question.point = qpoint
        question.header_text = qht
        question.footer_text = qft
        question.success_message = success_msg
        question.fail_message = fail_msg
        question.correct__answer = correct
        question.save()

        if type == "one_answer":
            choice1 = One_answer()
            choice2 = One_answer()
            choice3 = One_answer()

            choice1.question = question
            choice1.answer_variant = request.POST['answ_variant1']
            choice1.answer_description = request.POST['answ_desc1']
            choice1.point = request.POST['point1']
            choice1.save()
            choice2.question = question
            choice2.answer_variant = request.POST['answ_variant2']
            choice2.answer_description = request.POST['answ_desc2']
            choice2.point = request.POST['point2']
            choice2.save()
            choice3.question = question
            choice3.answer_variant = request.POST['answ_variant3']
            choice3.answer_description = request.POST['answ_desc3']
            choice3.point = request.POST['point3']
            choice3.save()

        elif type == "free_text":
            text = request.POST['text']

            choice = Free_Text()

            choice.question = question
            choice.text = text
            choice.save()

        else:
            choice1 = Multichoice()
            choice2 = Multichoice()
            choice3 = Multichoice()

            choice1.question = question
            choice1.multi_variant = request.POST['answer_variant1']
            choice1.multi_descp = request.POST['multidescp1']
            choice1.point = request.POST['pointn1']
            choice1.save()

            choice2.question = question
            choice2.multi_variant = request.POST['answer_variant2']
            choice2.multi_descp = request.POST['multidescp2']
            choice2.point = request.POST['pointn2']
            choice2.save()

            choice3.question = question
            choice3.multi_variant = request.POST['answer_variant3']
            choice3.multi_descp = request.POST['multidescp3']
            choice3.point = request.POST['pointn3']
            choice3.save()

        return render(request, 'exam/index.html')
    else:
        return render(request, 'exam/create_question.html')


# afficher la liste des questions pour ajouter les boutons edit et delete
def affich_question(request, exam_id):
    exam = Exam.objects.get(pk=exam_id)
    question = exam.question_set.all()
    context = {'exam': exam}
    # context = {'question': question}
    return render(request, 'exam/question_list.html', context)


# supprimer une question
def delete_question(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    question.delete()
    return render(request, 'exam/index.html')


# edit questions
def edit_ONE(request, question_id):
    question = Question.objects.get(pk=question_id)
    if request.method == 'POST':
        question.description = request.POST['desc']
        question.point = request.POST['point']
        question.header_text = request.POST['qht']
        question.footer_text = request.POST['qft']
        question.success_message = request.POST['success_msg']
        question.fail_message = request.POST['fail_msg']
        question.save()

        x = request.POST.get('id1', False)
        y = request.POST.get('id2', False)
        z = request.POST.get('id3', False)

        ans1 = get_object_or_404(One_answer, pk=x)
        ans2 = get_object_or_404(One_answer, pk=y)
        ans3 = get_object_or_404(One_answer, pk=z)
        ans1.answer_variant = request.POST.get('answer_variant1', False)
        ans1.answer_description = request.POST.get('answer_desc1', False)
        ans1.point = request.POST.get('point1', False)

        ans1.answer_variant = request.POST['answer_variant1']
        ans1.answer_description = request.POST['answer_description1']
        ans1.point = request.POST['point1']
        ans1.save()

        answ_variant2 = request.POST['answer_variant2']
        answ_desc2 = request.POST['answer_description2']
        point2 = request.POST['point2']
        ans2.answer_variant = answ_variant2
        ans2.answer_description = answ_desc2
        ans2.point = point2
        ans2.save()
        answ_variant3 = request.POST['answer_variant3']
        answ_desc3 = request.POST['answer_description3']
        point3 = request.POST['point3']
        ans3.answer_variant = answ_variant3
        ans3.answer_description = answ_desc3
        ans3.point = point3
        ans3.save()
        return render(request, 'exam/index.html')
    else:
        context = {'question': question}
        return render(request, 'exam/modif_ONE.html', context)


def edit_MULTI(request, question_id):
    question = Question.objects.get(pk=question_id)
    if request.method == 'POST':
        question.description = request.POST['desc']
        question.point = request.POST['point']
        question.header_text = request.POST['qht']
        question.footer_text = request.POST['qft']
        question.success_message = request.POST['success_msg']
        question.fail_message = request.POST['fail_msg']
        question.save()

        x = request.POST.get('id1', False)
        y = request.POST.get('id2', False)
        z = request.POST.get('id3', False)

        ans1 = get_object_or_404(Multichoice, pk=x)
        ans2 = get_object_or_404(Multichoice, pk=y)
        ans3 = get_object_or_404(Multichoice, pk=z)
        ans1.answer_variant = request.POST.get('answer_variant1', False)
        ans1.answer_description = request.POST.get('answer_desc1', False)
        ans1.point = request.POST.get('point1', False)

        ans1.answer_variant = request.POST['answer_variant1']
        ans1.answer_description = request.POST['answer_desc1']
        ans1.point = request.POST['point1']
        ans1.save()

        ans2.answer_variant = request.POST['answer_variant2']
        ans2.answer_description = request.POST['answer_desc2']
        ans2.point = request.POST['point2']
        ans2.save()

        ans3.answer_variant = request.POST['answer_variant3']
        ans3.answer_description = request.POST['answer_desc3']
        ans3.point = request.POST['point3']
        ans3.save()
        return render(request, 'exam/index.html')
    else:
        context = {'question': question}
        return render(request, 'exam/modif_MULTI.html', context)


def edit_FREE(request, question_id):
    question = Question.objects.get(pk=question_id)
    if request.method == 'POST':
        question.description = request.POST['description']
        question.point = request.POST['point']
        question.header_text = request.POST['qht']
        question.footer_text = request.POST['qft']
        question.success_message = request.POST['success_msg']
        question.fail_message = request.POST['fail_msg']
        question.save()
        x = request.POST['id']
        t = Free_Text.objects.get(pk=x)
        t.text = request.POST['text']
        t.save()
        return render(request, 'exam/index.html')
    else:
        context = {'question': question}
        return render(request, 'exam/modif_FREE.html', context)


# try_exam


listevide = []


def preparation(request, exam_id):
    global listevide
    exam = Exam.objects.get(pk=exam_id)
    L1 = Question.objects.filter(ex=exam).values_list('id', flat=True)
    # stockage de chq liste dans la session de user
    request.session['question_ids'] = sample(list(L1), len(L1))  # aleatoire

    return render(request, 'exam/start_exam.html', {'exam': exam})


# sera appelée dans save_response to pass from question to another
def pass_exam(request, exam_id, indice):
    global listevide
    question_ids = request.session.get('question_ids')
    indice = int(indice) if not isinstance(indice, int) else indice
    id = question_ids[indice]
    exam = Exam.objects.get(pk=exam_id)
    q = Question.objects.get(pk=id)  # get 1 question which its id in the liste_id
    context = {'indice': indice, 'q': q, 'question_ids': question_ids,
               'exam_id': exam_id,'exam': exam, 'listevide': listevide}
    return render(request, 'exam/pass_exam.html', context)



# SAVE response in database
def save_response(request, exam_id, indice):
    if request.POST:
        global listevide
        question_ids = request.session.get('question_ids')

        ans = Answer()
        ans.exam = Exam.objects.get(pk=exam_id)
        indice = int(indice) if not isinstance(indice, int) else indice

        id = question_ids[indice]
        listevide.append(id)
        print(listevide)

        us = request.user
        ans.user = us
        if "radios" in request.POST:
            selected_choice = request.POST.get('radios')
            essay = One_answer.objects.get(pk=selected_choice)
            ans.One_answer = essay
            ans.score_question = essay.point
            ans.save()

        elif "radiosM" in request.POST:
            selected_choice = request.POST.get('radiosM')
            essay = Multichoice.objects.get(pk=selected_choice)
            ans.multi_choice_answer = essay
            ans.score_question = essay.point
            ans.save()
        else:
            text = request.POST.get('text')
            ans.free_text = text
            ans.save()
        limit_index = Question.objects.filter(ex_id=exam_id).count() - 1
        if indice < limit_index:
            indice = indice + 1
        else:
            # return redirect('/exam/exam_id/score')
            listevide[:] = []
            return score(request, exam_id)
        return pass_exam(request, exam_id, indice)
    else:
        return pass_exam(request, exam_id, indice)


def score(request, exam_id):
    SCORE = 0
    exam = Exam.objects.get(pk=exam_id)
    score_list = list(Answer.objects.all())
    for i in score_list:
        SCORE += i.score_question
    print(SCORE)
    context = {'SCORE': SCORE, 'exam': exam}
    return render(request, 'exam/resultPROF.html', context)


# add some LOCAL users(exist in the database) to my group, invite others if I have their emails

def addlocal_stu(request):
    if request.POST:
        grp = Groupst()
        grp.professor = request.user
        x = request.POST['id_us']
        stu = User.objects.get(email=x)
        grp.student = stu
        grp.save()
        return render(request, 'exam/MYstudents.html')
    else:
        users = User.objects.all()
        return render(request, 'exam/all_users.html', {'userLIST': users})


def addstranger_stu(request):
    if request.POST:
        recipient_list = request.POST['TO']
        msg = request.POST['message']
        send_mail('invitation',
                  msg,
                  'quiz@ghazelatc.com',
                  # ['brikimaroua.090696@gmail.com'],
                  [recipient_list],
                  fail_silently=False
                  )
        st = User.objects.get(email='recipient_list')
        grp = Groupst()
        grp.professor = request.user
        grp.student = st
        grp.save()
        return render(request, 'exam/index.html')
    else:
        return render(request, 'exam/send_mail.html')


# affect an exam to my students
def assignTO_exam(request):
    if request.POST:
        affectation = Groupst()
        affectation.professor = request.user
        a = request.POST['emailst']
        affectation.student = User.objects.get(email=a)
        # affectation.student = Groupst.student.objects.get(email=a)
        # just be simple ('user)
        if "drop" in request.POST:
            selected_ex = request.POST['drop']
            print(selected_ex)
            affectation.assigned_exam = Exam.objects.get(pk=int(selected_ex))
        affectation.save()
        return redirect('/exam/index')
    else:
        grp = Groupst.objects.filter(professor=request.user)
        exams = Exam.objects.filter(prof=request.user)
        context = {'grp': grp, 'exams': exams}
        return render(request, 'exam/MYstudents.html', context)


# first try for the function send mail
def send(request):
    list = []
    if request.POST:
        subj = request.POST['subject']
        msg = request.POST['message']
        from_email = request.POST['FROM']
        recipient_list = request.POST['TO']
        list.append(recipient_list)
        send_mail('object',
                  msg,
                  'quiz@ghazelatc.com',
                  ['brikimaroua.090696@gmail.com'],
                  fail_silently=False
                  )

        if subj and msg and from_email:
            send_mail(subj, msg, from_email, list)
            return render(request, 'exam/index.html')
        else:
            return HttpResponse('Make sure all fields are entered and valid.')
    else:
        return render(request, 'exam/send_mail.html')


#
# def send(request):
#     message='you will find below a link signup to become a member of my group http://127.0.0.1:8000/authentification/signup'
#     subject = 'join my group'
#     from_email = 'quiz@ghazelatc.com'
#     to = ['brikimaroua.090696@gmail.com']
#     send_mail(subject, message, from_email, to)
#     return render(request, 'exam/index.html')


def homeUSER(request):
    # exam = Exam.objects.get(pk=exam_id)

    return render(request, 'exam/indexUSER.html')


"""exam modes : training---->with timer
                        ---->without timer
                pass real exam------> with timer of course"""


# first of all I thought that the student is going to choose the mode he want
# the professor will enter the mode of exam else the student can try the same exam he will pass and that's not fair of course
def choose_mode(request):
    G = []
    if request.POST:
        exam = Exam()
        exam.mode = request.POST['']
        pass
    else:
        GRP = list[Groupst.objects.filter(professor=request.user)]
        # x = GRP.assigned_exam
        context = {'GRP': GRP}
        return render(request, 'exam/chooseMODE.html', context)


"""def dbsaveSTUD(request, exam_id, question_id):
    bool = True  # indique le mode de passage de l'examen True=real exam
    if request.POST:
        if bool == True:
            ans = Answer()
            ans.exam = Exam.objects.get(pk=exam_id)
            us = request.user
            ans.user = us
            if "radios" in request.POST:
                selected_choice = request.POST['radios']
                essay = One_answer.objects.get(pk=selected_choice)
                ans.One_answer = essay
                ans.score_question = essay.point
                ans.save()
            elif "radiosM" in request.POST:
                selected_choice = request.POST['radiosM']
                essay = Multichoice.objects.get(pk=selected_choice)
                ans.multi_choice_answer = essay
                ans.score_question += essay.point
                ans.save()
            else:
                text = request.POST['text']
                ans.free_text = text
                ans.save()
            return render(request, "exam/stud_pass_exam.html")
        else:

            if 1 == 1:
                # if training with timer is selected
                # correction will be displayed
                ans = Answer()
                ans.exam = Exam.objects.get(pk=exam_id)
                us = request.user
                ans.user = us
                if "radios" in request.POST:
                    selected_choice = request.POST['radios']
                    essay = One_answer.objects.get(pk=selected_choice)
                    ans.One_answer = essay
                    ans.score_question = essay.point
                    ans.save()

                elif "radiosM" in request.POST:
                    selected_choice = request.POST['radiosM']
                    essay = Multichoice.objects.get(pk=selected_choice)
                    ans.multi_choice_answer = essay
                    ans.score_question += essay.point
                    ans.save()
                else:
                    text = request.POST['text']
                    ans.free_text = text
                    ans.save()
                # return render(request, "exam/trainingWITHtimer.html")
            else:
                pass
                # training without timer
                return (render(request, 'exam/trainingWITHOUTtimer.html'))
    else:
        pass"""

liste1 = []
liste2 = []
liste3 = []

def preparationSTUD(request, exam_id):
    exam = Exam.objects.get(pk=exam_id)
    L1 = Question.objects.filter(ex=exam).values_list('id', flat=True)
    # stockage de chq liste dans la session de user
    request.session['question_ids'] = sample(list(L1), len(L1))  # aleatoire
    return render(request, 'exam/start_examSTUD.html', {'exam': exam})

# pass the question index in the random list passed in the session of the user ---->foreach exam mode
def pass_examSTUD(request, exam_id, indice):
    exam = Exam.objects.get(pk=exam_id)
    if exam.mode == 'training':
        global liste1
        question_ids = request.session.get('question_ids')
        indice = int(indice) if not isinstance(indice, int) else indice
        b = indice
        id = question_ids[indice]
        q = Question.objects.get(pk=id)  # get 1 question which its id in the liste_id
        context = {'indice': indice, 'q': q, 'question_ids': question_ids,
                   'exam_id': exam_id, 'liste1': liste1}
        return render(request, 'exam/modetraining2.html', context)
    elif exam.mode == 'certified_exam':
        global liste2
        question_ids = request.session.get('question_ids')
        indice = int(indice) if not isinstance(indice, int) else indice
        b = indice
        id = question_ids[indice]
        q = Question.objects.get(pk=id)  # get 1 question which its id in the liste_id
        exam.is_passed = True
        context2 = {'indice': indice, 'q': q, 'question_ids': question_ids,
                    'exam_id': exam_id, 'liste2': liste2}
        return render(request, 'exam/certified_exam.html', context2)
    else:
        global liste3
        question_ids = request.session.get('question_ids')
        indice = int(indice) if not isinstance(indice, int) else indice
        id = question_ids[indice]
        q = Question.objects.get(pk=id)  # get 1 question which its id in the liste_id
        exam.is_passed = True
        context3 = {'indice': indice, 'q': q, 'question_ids': question_ids,
                   'exam_id': exam_id, 'liste3': liste3}
        return render(request, 'exam/non_certifiedEXAM.html', context3)


# SAVE response in database
def save_responseSTUD(request, exam_id, indice):
    exam = Exam.objects.get(pk=exam_id)
    if exam.mode == 'training':
        if request.POST:
            global liste1
            question_ids = request.session.get('question_ids')
            ans = Answer()
            ans.exam = Exam.objects.get(pk=exam_id)
            indice = int(indice) if not isinstance(indice, int) else indice
            id = question_ids[indice]
            liste1.append(id)
            # print(liste1)
            us = request.user
            ans.user = us
            if "radios" in request.POST:
                selected_choice = request.POST.get('radios')
                essay = One_answer.objects.get(pk=selected_choice)
                ans.One_answer = essay
                ans.score_question = essay.point
                ans.save()
            elif "radiosM" in request.POST:
                selected_choice = request.POST.get('radiosM')
                essay = Multichoice.objects.get(pk=selected_choice)
                ans.multi_choice_answer = essay
                ans.score_question = essay.point
                ans.save()
            else:
                text = request.POST.get('text')
                ans.free_text = text
                ans.save()
            limit_index = Question.objects.filter(ex_id=exam_id).count() - 1
            if indice < limit_index:
                indice = indice + 1
            else:
                liste1[:] = []

                return score(request, exam_id)

            return pass_examSTUD(request, exam_id, indice)
        else:
            return pass_examSTUD(request, exam_id, indice)
    elif exam.mode == 'certified_exam':
        if request.POST:
            global liste2
            question_ids = request.session.get('question_ids')
            ans = Answer()
            ans.exam = Exam.objects.get(pk=exam_id)
            indice = int(indice) if not isinstance(indice, int) else indice
            print(indice)
            id2 = question_ids[indice]
            print(id2)
            liste2.append(id2)
            print(liste2)

            us = request.user
            ans.user = us
            if "radios" in request.POST:
                selected_choice = request.POST.get('radios')
                essay = One_answer.objects.get(pk=selected_choice)
                ans.One_answer = essay
                ans.score_question = essay.point
                ans.save()

            elif "radiosM" in request.POST:
                selected_choice = request.POST.get('radiosM')
                essay = Multichoice.objects.get(pk=selected_choice)
                ans.multi_choice_answer = essay
                ans.score_question = essay.point
                ans.save()
            else:
                text = request.POST.get('text')
                ans.free_text = text
                ans.save()
            limit_index = Question.objects.filter(ex_id=exam_id).count() - 1
            if indice < limit_index:
                indice = indice + 1
            else:
                liste2[:] = []  # when user finish the exam liste2(which contains answered questions will be full) so the color green will persist because it is a global variable so I have to empty it the same for listevide liste1 and liste3
                return certif(request, exam_id)
            return pass_examSTUD(request, exam_id, indice)
        else:
            return pass_examSTUD(request, exam_id, indice)

    else:
        if request.POST:
            global liste3
            question_ids = request.session.get('question_ids')
            ans = Answer()
            ans.exam = Exam.objects.get(pk=exam_id)
            indice = int(indice) if not isinstance(indice, int) else indice
            id3 = question_ids[indice]
            liste3.append(id3)
            us = request.user
            ans.user = us
            if "radios" in request.POST:
                selected_choice = request.POST.get('radios')
                essay = One_answer.objects.get(pk=selected_choice)
                ans.One_answer = essay
                ans.score_question = essay.point
                ans.save()
            elif "radiosM" in request.POST:
                selected_choice = request.POST.get('radiosM')
                essay = Multichoice.objects.get(pk=selected_choice)
                ans.multi_choice_answer = essay
                ans.score_question = essay.point
                ans.save()
            else:
                text = request.POST.get('text')
                ans.free_text = text
                ans.save()
            limit_index = Question.objects.filter(ex_id=exam_id).count() - 1
            if indice < limit_index:
                indice = indice + 1
            else:
                liste3[:] = []

                return score_user(request, exam_id)

            return pass_examSTUD(request, exam_id, indice)
        else:
            return pass_examSTUD(request, exam_id, indice)


def score_user(request, exam_id):
    SCORE = 0
    exam = Exam.objects.get(pk=exam_id)
    score_list = list(Answer.objects.all())
    for i in score_list:
        SCORE += i.score_question
    print(SCORE)
    context = {'SCORE': SCORE, 'exam': exam}
    return render(request, 'exam/resultSTU.html', context)


# if te user pass a certified exam he must to get a score out of success score(entered by the professor)
def certif(request, exam_id):
    SCORE = 0
    exam = Exam.objects.get(pk=exam_id)
    score_list = list(Answer.objects.all())
    for i in score_list:
        SCORE += i.score_question
    print(SCORE)
    if SCORE > exam.success_score and exam.mode == 'certified_exam':
        student = request.user
        print(student)
        return render(request, 'exam/certificat.html', {'exam': exam, 'student': student})
    else:
        context = {'SCORE': SCORE, 'exam': exam}
        return render(request, 'exam/resultSTU.html', context)


def correction(request, exam_id):
    exam = Exam.objects.get(pk=exam_id)
    # if not exam.is_passed:
    questions = Question.objects.filter(ex=exam_id)
    context = {'exam': exam, 'questions': questions}
    return render(request, 'exam/correction.html', context)


def STUD_EXAMS(request):
    if request.user.is_authenticated:
        us = request.user
        stud = Groupst.objects.filter(student=us)
        return render(request, 'exam/STUD_EXAMS.html', {'stud': stud})





def becomePROF(request):
    if request.user.is_authenticated:
        print('xxxxxxxxxxxxxxxxxxxxx')
        profile = Profile.objects.get(user=request.user)
        profile.is_professor = True
        profile.save()
        return render(request, 'exam/index.html')
    else:
        return render(request, 'registration/login.html')
