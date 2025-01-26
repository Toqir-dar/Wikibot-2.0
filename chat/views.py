from django.shortcuts import render, HttpResponse, redirect

def index(request):
    return render(request,'index.html')

def chat1(request):
    if request.method == 'GET':
        return render(request, 'chat.html')
    if request.method == 'POST':
        if 'conversation' not in request.session:
            request.session['conversation'] = []
        query = request.POST.get('input_text')
        if 'clear' in query.lower().strip():
            request.session.clear()
            return render(request, 'chat.html')
        # Hugging face Access token: 
        from langchain_huggingface import HuggingFaceEndpoint
        import os
        HF_token = os.environ.get['HF_token']
        repo_id = 'mistralai/Mistral-7B-Instruct-v0.3'
        llm = HuggingFaceEndpoint(repo_id = repo_id, temperature = 0.6,model_kwargs={"token":HF_token,'max_length':70})
        # import markdown
        response = (llm.invoke(query))
        # response = markdown.markdown(response)  
        try:
            if query != None and response != None:
                request.session['conversation'].append({'user': query, 'bot': response})
                request.session.modified = True
            else:
                raise ValueError
        except:
            response = "Didn't understand! Try again"
            request.session['conversation'].append({'user': query, 'bot': response})
            request.session.modified = True
            
        return render(request, 'chat.html', {'conversation': request.session['conversation']})
