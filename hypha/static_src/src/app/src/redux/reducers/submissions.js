import { combineReducers } from 'redux';

import {
    CLEAR_CURRENT_SUBMISSION,
    FAIL_LOADING_SUBMISSION,
    START_LOADING_SUBMISSION,
    UPDATE_SUBMISSIONS_BY_ROUND,
    UPDATE_SUBMISSION,
    SET_CURRENT_SUBMISSION,
    UPDATE_BY_STATUSES,
    START_EXECUTING_SUBMISSION_ACTION,
    FAIL_EXECUTING_SUBMISSION_ACTION,
} from '@actions/submissions';

import { CREATE_NOTE, UPDATE_NOTES, UPDATE_NOTE } from '@actions/notes'


function submission(state={comments: []}, action) {
    switch(action.type) {
        case START_LOADING_SUBMISSION:
            return {
                ...state,
                isFetching: true,
                isErrored: false,
            };
        case FAIL_LOADING_SUBMISSION:
            return {
                ...state,
                isFetching: false,
                isErrored: true,
            };
        case UPDATE_SUBMISSION:
            return {
                ...state,
                ...action.data,
                isFetching: false,
                isErrored: false,
                isExecutingAction: false,
                isExecutingActionErrored: false,
                executionActionError: undefined,
                changedLocally: action.changedLocally === true
            };
        case UPDATE_NOTES:
            return {
                ...state,
                comments: action.data.results
                    .map(note => note.id)
                    .filter(id => !state.comments.includes(id))
                    .concat(state.comments)
            };
        case START_EXECUTING_SUBMISSION_ACTION:
            return {
                ...state,
                isExecutingAction: true,
                isExecutingActionErrored: false,
                executionActionError: undefined,
            };
        case FAIL_EXECUTING_SUBMISSION_ACTION:
            return {
                ...state,
                isExecutingAction: false,
                isExecutingActionErrored: true,
                executionActionError: action.error
            };
        case UPDATE_NOTE:
            return {
                ...state,
                comments: [
                    action.data.id,
                    ...(state.comments.filter(comment => comment !== action.note.id) || []),
                ]
            };
        case CREATE_NOTE:
            return {
                ...state,
                comments: [
                    action.data.id,
                    ...(state.comments || []),
                ]
            };
        default:
            return state;
    }
}


function submissionsByID(state = {}, action) {
    switch(action.type) {
        case START_LOADING_SUBMISSION:
        case FAIL_LOADING_SUBMISSION:
        case UPDATE_SUBMISSION:
        case CREATE_NOTE:
        case UPDATE_NOTE:
        case UPDATE_NOTES:
        case START_EXECUTING_SUBMISSION_ACTION:
        case FAIL_EXECUTING_SUBMISSION_ACTION:
            return {
                ...state,
                [action.submissionID]: submission(state[action.submissionID], action),
            };
        case UPDATE_BY_STATUSES:
        case UPDATE_SUBMISSIONS_BY_ROUND:
            return {
                ...state,
                ...action.data.results.reduce((newItems, newSubmission) => {
                    newItems[newSubmission.id] = submission(
                        state[newSubmission.id],
                        {
                            type: UPDATE_SUBMISSION,
                            data: newSubmission,
                        }
                    );
                    return newItems;
                }, {}),
            };
        default:
            return state;
    }
}


function currentSubmission(state = null, action) {
    switch(action.type) {
        case SET_CURRENT_SUBMISSION:
            return action.id;
        case CLEAR_CURRENT_SUBMISSION:
            return null;
        default:
            return state;
    }
}


const submissions = combineReducers({
    byID: submissionsByID,
    current: currentSubmission,
});

export default submissions;
