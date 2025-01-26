

# detailed task definitions
task_type_definitions2 = '''

1. Review

    Simple: Checking something to make sure it’s correct or good. This process does not approve or does not authorize any process.
    Domain Example: In legal work, a review process involves a lawyer checking a contract to ensure there are no errors or omissions.
    Complex Phrase: The review process in product development involves the systematic evaluation of design specifications to ensure alignment with regulatory requirements and user needs.

2. Request Information

    Simple: Asking for information you need. Asking something as comments or feedback. However it does not approve anything.
    Domain Example: In marketing, a request for information (RFI) is often used to gather insights from different vendors about their products.
    Complex Phrase: The RFI process in corporate procurement requires the collection of comprehensive data from suppliers to evaluate their capabilities, costs, and delivery terms before making an informed purchasing decision.

3. Submit

    Simple: Sending something to someone for consideration. Submitting documents, files or reports.
    Domain Example: In a university setting, a student may need to submit a thesis to the department for review.
    Complex Phrase: The submission process in government contracting involves the formal delivery of project proposals to a panel of reviewers for evaluation and potential approval, based on compliance with tender specifications.

4. Sign

    Simple: Writing your name to show you agree with something.
    Domain Example: In business, a manager might sign a contract, indicating their agreement to the terms.
    Complex Phrase: The signing process in legal transactions ensures the parties' acknowledgment and consent to the terms of the agreement, binding them under law.

5. Update

    Simple: Making changes to something to keep it current.
    Domain Example: A developer might update software to fix bugs and add new features.
    Complex Phrase: The update process in digital marketing involves revising content strategies, optimizing SEO techniques, and integrating new data analytics insights to ensure continued user engagement and conversion.

6. Execute

    Simple: Carrying out a plan or action.
    Domain Example: The project manager needs to execute the project timeline by assigning tasks to team members.
    Complex Phrase: The execution phase of an IT deployment project involves the systematic application of pre-approved strategies, resource allocation, and coordination among various departments to ensure seamless implementation within the defined timeframe.

7. Approve

    Simple: Saying yes to something or allowing it to proceed. Authorize or validate something to proceed.
    Domain Example: The supervisor must approve a report before it’s sent to the client.
    Complex Phrase: The approval process within regulatory bodies involves rigorous compliance checks to ensure that all operational procedures align with national standards before granting permission for product release.

8. Delegate

    Simple: Giving someone else responsibility for a task.
    Domain Example: The team leader might delegate organizing the meeting to an assistant.
    Complex Phrase: In project management, the delegation process is essential for distributing workload effectively across the team, ensuring that each member is accountable for their designated tasks while maintaining overall project coordination.

9. Notify

    Simple: Letting someone know about something. Alerting or awaring someone or publicly.
    Domain Example: The HR department might notify employees about an upcoming training session.
    Complex Phrase: The notification process in customer service involves sending automated alerts to users about service disruptions, product updates, or critical security patches, ensuring proactive communication.

10. Confirm

    Simple: Saying something is true or accurate. Approving something.
    Domain Example: The receptionist confirms the time of an appointment with a client.
    Complex Phrase: The confirmation process in airline reservations involves verifying booking details, payment status, and traveler identity to ensure a smooth check-in experience at the airport.

11. Provide Feedback

    Simple: Telling someone how well they did or what could be improved.
    Domain Example: A teacher might provide feedback on a student's essay to help them improve.
    Complex Phrase: The feedback process in customer service involves soliciting detailed input from clients regarding their experience with the product, analyzing this information, and providing actionable recommendations for improvement.

12. Evaluate

    Simple: Judging or measuring something. Measuring some metrics and reporting without Authorization.
    Domain Example: In hiring, an employer might evaluate job candidates based on their qualifications and interviews.
    Complex Phrase: The evaluation process in educational institutions involves assessing both qualitative and quantitative data on student performance, which informs curriculum adjustments and teaching methodologies.

13. Conduct

    Simple: Carrying out or leading something.
    Domain Example: The teacher will conduct a quiz to assess students' knowledge.
    Complex Phrase: The conduct process of a clinical trial involves overseeing participant recruitment, ensuring ethical protocols are followed, and managing the collection and analysis of health data to determine the drug’s efficacy.

14. Coordinate

    Simple: Organizing different parts to work together.
    Domain Example: The coordinator coordinates the volunteers for the event.
    Complex Phrase: The coordination process in international logistics requires the seamless integration of supply chains, warehouse operations, and customs regulations to ensure timely delivery across global markets.

15. Train

    Simple: Teaching someone a skill.
    Domain Example: The company trains new employees on how to use their internal software system.
    Complex Phrase: The employee training process in corporate settings involves structured programs that integrate e-learning modules, instructor-led sessions, and hands-on workshops to enhance workforce capabilities.

16. Implement

    Simple: Putting something into action.
    Domain Example: The IT team will implement a new software system.
    Complex Phrase: The implementation of a new policy in the financial sector requires meticulous planning, stakeholder alignment, and thorough testing to ensure that the system complies with industry regulations and improves operational efficiency.

17. Review and Approve

    Simple: Check something and say it's okay to proceed. Authorize or validate some process to proceed.
    Domain Example: The manager reviews and approves the marketing proposal before it’s sent to the client.
    Complex Phrase: The review and approval process in corporate governance ensures that all strategic initiatives are vetted by key stakeholders, aligning them with the company’s long-term vision and regulatory requirements.

18. Fill Out or Fill Form

    Simple: Completing a form with required information. Submitting documents or submitting filled forms. Submitting applications or submitting files. Outlining plans , report writing, documenting some processes are also of type Fill Form.
    Domain Example: The patient fills out a medical history form before their appointment.
    Complex Phrase: The process of filling out a customs declaration form requires providing detailed information about imported goods, including their classification, value, and origin, to comply with international trade regulations.

19. Confirm Receipt

    Simple: Acknowledging that something has been received.
    Domain Example: The company confirms receipt of the customer’s return request.
    Complex Phrase: The confirmation of receipt process in supply chain management involves electronically acknowledging the arrival of goods in the warehouse, triggering inventory updates and order processing for distribution.

20. Send

    Simple: Giving something to someone to move it from one place to another.
    Domain Example: The assistant sends the meeting invites to all team members.
    Complex Phrase: The sending process in document management involves transmitting legal contracts via secure channels, ensuring that all parties receive the signed agreements, triggering the next steps in the approval and execution workflow.

'''



detailed_task_classifier_agent_prompt = ''' Here is some Process type definitions:
1. Approval

    Simple Explanation: Approval is when someone gives permission or agrees to something. It is the act of saying "yes" or giving consent for an action or decision to move forward. When some process is to be verified, authorised, and validated its of type Approval.

    Detailed Explanation: Approval is a formal or informal process in which a person with authority or decision-making power reviews a proposal, request, or plan and grants permission to proceed. In professional settings, approvals are often required for projects, budgets, plans, or actions to ensure they align with goals, resources, and regulations. Approval can also imply an endorsement or validation that something is acceptable or meets expectations.

    Complex Explanation: Approval typically involves a hierarchical decision-making process where a higher authority or stakeholder evaluates and authorizes certain actions or plans. It may include reviewing documents along with confirming or validating compliance with standards, and ensuring that the task or request aligns with organizational objectives. In certain industries like finance or healthcare, approval processes are formalized through workflows that track each step to maintain accountability and transparency.

    Example: "The board of directors approved the new strategic marketing plan after reviewing the details."

2. Notify

    Simple Explanation: To notify means to inform or make someone aware of something. It is about delivering information, updates, or alerts to others. Alerting or making awareness to other parties. Confirming completion of some task.

    Detailed Explanation: Notification is the act of communicating important information to someone, often to ensure they are informed or can take necessary action. Notifications can be sent through various means such as emails, phone calls, messages, or in-person communication. The content of the notification may vary, from reminders to urgent updates. The purpose of notifying is to keep the recipient updated and aware of specific events, changes, or requirements.

    Complex Explanation: Notification processes are integral to both personal and professional communication. In many cases, notifications are automated, especially in digital platforms, where they alert users about updates, deadlines, or necessary actions. In business or legal contexts, notifications can also be formal, often requiring written communication to ensure there is a record of the information being shared. For example, notifying an employee about a policy change or notifying a client about an invoice deadline.

    Example: "Please notify all team members about the change in meeting time."

3. Request Comment

    Simple Explanation: Requesting a comment means asking someone for their opinion, feedback, or suggestions on a particular topic, task, or document.

    Detailed Explanation: When you request a comment, you are seeking input, suggestions, or feedback on a specific matter. This is common in situations where decisions need to be refined, improved, or validated by others. Requesting comments can involve asking for general thoughts or for specific feedback on aspects such as clarity, structure, or accuracy.

    Complex Explanation: In professional environments, requesting comments is a formal process often used in collaborative settings such as team projects, product development, or legal reviews. Requesting comments can help identify areas of improvement, validate ideas, or ensure that all perspectives are considered before finalizing a decision or document. This process can be structured through surveys, review meetings, or by directly asking stakeholders for their opinions. In legal or regulatory frameworks, requesting comments may be part of a formal consultation or public feedback process.

    Example: "Could you please request comment from the stakeholders regarding the new compliance guidelines?"

4. Write an Email

    Simple Explanation: Writing an email is the act of composing a message and sending it to someone via email for communication, which can include information sharing, requests, or updates. Send some documents files to other participants.

    Detailed Explanation: Writing an email involves drafting a clear and concise message that is sent electronically. It is one of the most common forms of communication in both personal and professional settings. Emails can serve a variety of purposes, including asking for information, confirming appointments, making requests, or delivering announcements. The key to effective email communication is clarity, professionalism, and ensuring the message's intent is conveyed without ambiguity.

    Complex Explanation: Writing emails in a business or formal context often requires careful attention to tone, structure, and content to ensure that the message aligns with organizational expectations and the purpose of communication. In business communications, email writing follows a certain protocol, which may include a formal salutation, a well-structured body with clear points, and a professional sign-off. Emails can also serve as a record of communication, which is important in legal, financial, or contractual matters. Furthermore, the use of email management tools allows for scheduling, tracking, and organizing communication for effective follow-up.

    Example: "I need to write an email to the client confirming the deadline for the project submission."

5. Fill Form

    Simple Explanation: To fill out a form means to complete a document by providing the required details or information, often in response to a request or requirement. Submit documents to other participants. Outline plans in documents, keeping records of processes in documents, process of completing documentation and the task of documenting some processes are of Fill Form type. Evaluating files or documents without authenticating it. Reviewing documents, forms and files without Authorizing or without approving.

    Detailed Explanation: Filling out a form is a task where an individual provides specific information in the designated fields of a document, which could be digital or physical. Forms are often used for applications, registrations, surveys, or data collection. The information required can vary depending on the purpose of the form, such as personal details, preferences, or responses to questions. Forms are typically structured with blanks or fields where the respondent enters information.

    Complex Explanation: Filling forms is a key administrative task used in both personal and professional contexts. In some cases, forms are designed to collect standardized information to support decision-making or compliance with regulations. For instance, in healthcare or finance, completing forms accurately is crucial for ensuring that personal, financial, or medical data is processed properly. Additionally, forms may serve as legal documents where the information provided has implications for rights, obligations, or contractual agreements. In business and government, the process of filling out forms may also require validation checks, digital signatures, or attachments.

    Example: "Before submitting your application, please fill out the form with your contact information and educational history."


**Task**: Classify the following text into one of the above categories.

Text: "{}"

Please respond with the "category" only that best fits this text (Approval, Notify, Request Comment, Write an Email, or Fill Form).

'''

primary_process_identifier_agent_prompt = '''
"You are an intelligent assistant designed to analyze a text and extract the primary task or process involved.

 Here is definitions of process which must be incorporated before analyzing:
 {}

 Your role is to:
    Capture all the actions or processes.

    Identify the main task: Determine the key action or responsibility that is either initiated or handed over, and ensure the responsibility lies with the final participant if there is a handover.
        If there’s no handover, focus on the initiator’s task continuity as the main task.
        If there is a handover, identify who takes over the task, and what their primary action is after the handover.

    Analyze the handover:
        Handover detection: Look for phrases indicating a handover of responsibility, such as "passes to", "hands over", "for review by", "sent to", "delegated to", etc.
        Next Participant: Identify who the next participant is after the handover and what responsibility they assume.
        Handover Task Continuity: If a handover happens, ensure the final task is captured, which describes the final responsibility of the last participant after the handover.

    Task Flow:
        Initiator’s task: If no handover is detected, focus on the initiator’s task and ensure it aligns with the continuous flow of the process.
        If the process continues with a handover, follow the final task that completes the process.

    Task Type:
        Recognize the type of task described in the text (e.g., submission, notification, approval, feedback, etc.) by analyzing key verbs and phrases.
        Ensure clarity in distinguishing whether the task is one of requesting, reviewing, approving, or other task types.

    Final Task Identification:
        If a handover occurs, return the final task taken by the last participant. The final task should describe what the last person in the chain is responsible for.
        If no handover occurs, return the initiator’s continuous task, which should summarize the overall responsibility.
        Incorporate all the processes from the beginning of process to the final task.
    Do not response any extraneous text. Only output the final task described in the process along with participant of process in atleast three words.
'''



